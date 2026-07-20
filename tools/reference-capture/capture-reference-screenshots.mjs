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

const viewports =