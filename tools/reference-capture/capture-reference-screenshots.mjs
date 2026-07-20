import { chromium } from 'playwright';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import { fileURLToPath } from 'node:url';

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const repositoryRoot = path.resolve(scriptDirectory, '../..');
const manifestPath = path.join(scriptDirectory, 'routes.json');
const outputRoot = path.join(repositoryRoot, 'reference', 'screenshots');
const baseUrl = (process.env.REFERENCE_BASE_URL || 'https://albertroe2021-beep.github.io/tshirtswiss').replace(/\/$/, '');

const viewports = [
  { id: 'desktop', width: 1440, height: 1000, deviceScaleFactor: 1 },
  { id: 'tablet', width: 768, height: 1024, deviceScaleFactor: 1 },
  { id: 'mobile', width: 390, height: 844, deviceScaleFactor: 1 },
];

const supportedLanguages = ['en', 'de', 'fr'];
const navigationTimeout = Number(process.env.REFERENCE_NAVIGATION_TIMEOUT || 45000);
const settleDelay = Number(process.env.REFERENCE_SETTLE_DELAY || 1200);
const requestedRoute = process.env.REFERENCE_ROUTE || '';
const requestedLanguage = process.env.REFERENCE_LANGUAGE || '';
const requestedViewport = process.env.REFERENCE_VIEWPORT || '';

function validateManifest(manifest) {
  if (!manifest || !Array.isArray(manifest.routes)) {
    throw new Error('routes.json must contain a top-level routes array.');
  }

  for (const route of manifest.routes) {
    if (!route.id || typeof route.id !== 'string') {
      throw new Error('Each route must have a string id.');
    }

    if (!route.paths || typeof route.paths !== 'object') {
      throw new Error(`Route ${route.id} must define a paths object.`);
    }
  }
}

function shouldCaptureRoute(routeId) {
  return !requestedRoute || routeId === requestedRoute;
}

function shouldCaptureLanguage(language) {
  return !requestedLanguage || language === requestedLanguage;
}

function shouldCaptureViewport(viewportId) {
  return !requestedViewport || viewportId === requestedViewport;
}

async function ensureDirectory(directory) {
  await mkdir(directory, { recursive: true });
}

async function waitForPageToSettle(page) {
  await page.waitForLoadState('domcontentloaded');

  try {
    await page.waitForLoadState('networkidle', { timeout: 10000 });
  } catch {
    // Some pages keep analytics or background requests open. Continue after DOM load.
  }

  await page.evaluate(async () => {
    if (document.fonts?.ready) {
      await document.fonts.ready;
    }
  });

  await page.waitForTimeout(settleDelay);
}

async function captureScreenshot(page, route, language, viewport) {
  const relativePath = route.paths[language];

  if (!relativePath) {
    return {
      route: route.id,
      language,
      viewport: viewport.id,
      status: 'skipped',
      reason: 'No route path configured',
    };
  }

  const targetUrl = new URL(relativePath, `${baseUrl}/`).toString();
  const targetDirectory = path.join(outputRoot, language, route.id);
  const outputFile = path.join(targetDirectory, `${viewport.id}.png`);

  await ensureDirectory(targetDirectory);
  await page.setViewportSize({ width: viewport.width, height: viewport.height });

  const startedAt = Date.now();

  try {
    const response = await page.goto(targetUrl, {
      waitUntil: 'domcontentloaded',
      timeout: navigationTimeout,
    });

    await waitForPageToSettle(page);

    await page.screenshot({
      path: outputFile,
      fullPage: true,
      animations: 'disabled',
    });

    return {
      route: route.id,
      language,
      viewport: viewport.id,
      url: targetUrl,
      file: path.relative(repositoryRoot, outputFile).replaceAll(path.sep, '/'),
      width: viewport.width,
      height: viewport.height,
      httpStatus: response?.status() ?? null,
      status: response?.ok() === false ? 'captured-with-http-error' : 'captured',
      durationMs: Date.now() - startedAt,
      capturedAt: new Date().toISOString(),
    };
  } catch (error) {
    return {
      route: route.id,
      language,
      viewport: viewport.id,
      url: targetUrl,
      file: path.relative(repositoryRoot, outputFile).replaceAll(path.sep, '/'),
      status: 'failed',
      error: error instanceof Error ? error.message : String(error),
      durationMs: Date.now() - startedAt,
      capturedAt: new Date().toISOString(),
    };
  }
}

async function main() {
  const manifest = JSON.parse(await readFile(manifestPath, 'utf8'));
  validateManifest(manifest);

  const routes = manifest.routes.filter((route) => shouldCaptureRoute(route.id));
  const languages = supportedLanguages.filter(shouldCaptureLanguage);
  const selectedViewports = viewports.filter((viewport) => shouldCaptureViewport(viewport.id));

  if (routes.length === 0) {
    throw new Error(`No route matched REFERENCE_ROUTE=${requestedRoute}`);
  }

  if (languages.length === 0) {
    throw new Error(`No language matched REFERENCE_LANGUAGE=${requestedLanguage}`);
  }

  if (selectedViewports.length === 0) {
    throw new Error(`No viewport matched REFERENCE_VIEWPORT=${requestedViewport}`);
  }

  await ensureDirectory(outputRoot);

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    locale: 'en-US',
    colorScheme: 'light',
    reducedMotion: 'reduce',
    ignoreHTTPSErrors: false,
    deviceScaleFactor: 1,
  });

  const page = await context.newPage();
  const results = [];

  try {
    for (const route of routes) {
      for (const language of languages) {
        for (const viewport of selectedViewports) {
          process.stdout.write(`Capturing ${language}/${route.id}/${viewport.id} ... `);
          const result = await captureScreenshot(page, route, language, viewport);
          results.push(result);
          process.stdout.write(`${result.status}\n`);
        }
      }
    }
  } finally {
    await browser.close();
  }

  const summary = {
    baseUrl,
    generatedAt: new Date().toISOString(),
    total: results.length,
    captured: results.filter((item) => item.status === 'captured').length,
    capturedWithHttpError: results.filter((item) => item.status === 'captured-with-http-error').length,
    skipped: results.filter((item) => item.status === 'skipped').length,
    failed: results.filter((item) => item.status === 'failed').length,
    filters: {
      route: requestedRoute || null,
      language: requestedLanguage || null,
      viewport: requestedViewport || null,
    },
    results,
  };

  const manifestOutput = path.join(outputRoot, 'capture-manifest.json');
  await writeFile(manifestOutput, `${JSON.stringify(summary, null, 2)}\n`, 'utf8');

  process.stdout.write(`\nCapture manifest written to ${path.relative(repositoryRoot, manifestOutput)}\n`);

  if (summary.failed > 0) {
    process.exitCode = 1;
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
