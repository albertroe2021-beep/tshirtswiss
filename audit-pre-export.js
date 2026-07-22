#!/usr/bin/env node

/**
 * Pre-Export Audit: Compare live WordPress site to GitHub Pages reference
 * Captures screenshots and validates build quality before export
 */

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const OUTPUT_DIR = '/tmp/audit_screenshots';
const LIVE_BASE = 'http://localhost:8088';
const REFERENCE_BASE = 'http://localhost:9000'; // Static server for reference

const PAGES_TO_AUDIT = [
  { slug: '', name: 'Home (EN)', lang: 'en', path: '/' },
  { slug: 'products', name: 'Products (EN)', lang: 'en', path: '/products/' },
  { slug: 'services', name: 'Services (EN)', lang: 'en', path: '/services/' },
  { slug: 'industries', name: 'Industries (EN)', lang: 'en', path: '/industries/' },
  { slug: 'resources', name: 'Resources (EN)', lang: 'en', path: '/resources/' },
  { slug: 'about-us', name: 'About (EN)', lang: 'en', path: '/about-us/' },
  { slug: 'contact', name: 'Contact (EN)', lang: 'en', path: '/contact/' },
  { slug: 'home', name: 'Home (DE)', lang: 'de', path: '/de/home/' },
  { slug: 'home', name: 'Home (FR)', lang: 'fr', path: '/fr/home/' },
];

async function ensureDir(dir) {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

async function captureScreenshot(browser, url, filename) {
  try {
    const page = await browser.newPage({
      viewport: { width: 1280, height: 1024 }
    });
    
    await page.goto(url, { waitUntil: 'networkidle', timeout: 10000 }).catch(() => {});
    await page.waitForTimeout(1000);
    
    const filepath = path.join(OUTPUT_DIR, filename);
    await page.screenshot({ path: filepath, fullPage: true });
    
    // Get page title and body text snippet
    const title = await page.title().catch(() => 'NO TITLE');
    const bodyText = await page.textContent('body').catch(() => '');
    const snippet = bodyText ? bodyText.substring(0, 200) : 'NO BODY TEXT';
    
    await page.close();
    
    return {
      success: true,
      filename,
      title,
      snippet: snippet.replace(/\n/g, ' ').trim(),
      url
    };
  } catch (err) {
    return {
      success: false,
      filename,
      error: err.message,
      url
    };
  }
}

async function main() {
  await ensureDir(OUTPUT_DIR);
  
  console.log('\n=== TSHIRTSWISS PRE-EXPORT AUDIT ===\n');
  console.log('Capturing live WordPress and reference screenshots...\n');
  
  const browser = await chromium.launch();
  const results = [];
  
  for (const page of PAGES_TO_AUDIT) {
    const liveUrl = LIVE_BASE + page.path;
    const refUrl = REFERENCE_BASE + page.path;
    
    console.log(`Auditing: ${page.name}`);
    
    // Capture live
    const liveResult = await captureScreenshot(
      browser,
      liveUrl,
      `live-${page.lang}-${page.slug || 'home'}.png`
    );
    
    // Capture reference
    const refResult = await captureScreenshot(
      browser,
      refUrl,
      `ref-${page.lang}-${page.slug || 'home'}.png`
    );
    
    results.push({
      page: page.name,
      live: liveResult,
      reference: refResult
    });
    
    // Quick sanity check
    if (liveResult.success && refResult.success) {
      const liveEmpty = !liveResult.snippet || liveResult.snippet.length < 50;
      const refEmpty = !refResult.snippet || refResult.snippet.length < 50;
      
      console.log(`  ✓ Live: ${liveResult.title.substring(0, 40)}...`);
      console.log(`    Content: ${liveEmpty ? '❌ EMPTY' : '✓ ' + liveResult.snippet.substring(0, 80)}`);
      console.log(`  ✓ Reference: ${refResult.title.substring(0, 40)}...`);
      console.log(`    Content: ${refEmpty ? '⚠️  SPARSE' : '✓ ' + refResult.snippet.substring(0, 80)}`);
    } else {
      if (!liveResult.success) console.log(`  ❌ Live: ${liveResult.error}`);
      if (!refResult.success) console.log(`  ❌ Reference: ${refResult.error}`);
    }
    console.log('');
  }
  
  await browser.close();
  
  // Generate report
  console.log('\n=== AUDIT REPORT ===\n');
  
  let failures = 0;
  let passes = 0;
  
  for (const result of results) {
    const liveGood = result.live.success && result.live.snippet && result.live.snippet.length > 50;
    const refGood = result.reference.success && result.reference.snippet && result.reference.snippet.length > 50;
    
    if (liveGood && refGood) {
      console.log(`✅ ${result.page}: PASS (both have content)`);
      passes++;
    } else if (!liveGood && refGood) {
      console.log(`❌ ${result.page}: FAIL (live is empty, reference has content)`);
      failures++;
    } else if (liveGood && !refGood) {
      console.log(`⚠️  ${result.page}: WARNING (live has content, reference sparse)`);
    } else {
      console.log(`❌ ${result.page}: FAIL (both empty)`);
      failures++;
    }
  }
  
  console.log(`\n${passes} PASS, ${failures} FAIL\n`);
  
  if (failures > 0) {
    console.log('🛑 BUILD FAILED: Live site has empty/missing pages');
    console.log(`\nScreenshots saved to: ${OUTPUT_DIR}`);
    process.exit(1);
  } else {
    console.log('✅ BUILD PASSED: All audited pages have content');
    console.log(`\nScreenshots saved to: ${OUTPUT_DIR}`);
    process.exit(0);
  }
}

main().catch(err => {
  console.error('Audit error:', err);
  process.exit(2);
});
