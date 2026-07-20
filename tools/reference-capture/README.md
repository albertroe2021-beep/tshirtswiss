# TShirtSwiss Reference Capture Tool

This tool captures full-page screenshots of the live TShirtSwiss site so the Elementor rebuild can be compared against a permanent visual baseline.

## What it captures

For every configured route, the script captures:

- English, German and French variants
- Desktop at 1440 x 1000
- Tablet at 768 x 1024
- Mobile at 390 x 844
- Full-page PNG screenshots
- A machine-readable capture manifest

Screenshots are written to:

```text
reference/screenshots/<language>/<route>/<viewport>.png
```

The summary manifest is written to:

```text
reference/screenshots/capture-manifest.json
```

## Installation

From this directory:

```bash
npm install
npx playwright install chromium
```

## Capture all configured pages

```bash
npm run capture
```

By default the script captures from:

```text
https://albertroe2021-beep.github.io/tshirtswiss
```

## Capture from another deployment

Set `REFERENCE_BASE_URL` before running the command.

macOS or Linux:

```bash
REFERENCE_BASE_URL=https://example.com npm run capture
```

Windows PowerShell:

```powershell
$env:REFERENCE_BASE_URL="https://example.com"
npm run capture
```

## Capture a subset

The following optional environment variables can be combined:

- `REFERENCE_ROUTE` — route ID from `routes.json`
- `REFERENCE_LANGUAGE` — `en`, `de` or `fr`
- `REFERENCE_VIEWPORT` — `desktop`, `tablet` or `mobile`

Example:

```bash
REFERENCE_ROUTE=home REFERENCE_LANGUAGE=de REFERENCE_VIEWPORT=mobile npm run capture
```

Windows PowerShell:

```powershell
$env:REFERENCE_ROUTE="home"
$env:REFERENCE_LANGUAGE="de"
$env:REFERENCE_VIEWPORT="mobile"
npm run capture
```

## Timing controls

Two optional environment variables control page loading behaviour:

- `REFERENCE_NAVIGATION_TIMEOUT` — navigation timeout in milliseconds; default `45000`
- `REFERENCE_SETTLE_DELAY` — delay after fonts and network activity settle; default `1200`

## Route manifest

Routes are configured in `routes.json`.

Each route requires a stable ID and a language-specific path:

```json
{
  "id": "home",
  "paths": {
    "en": "/pages/",
    "de": "/de/home/",
    "fr": "/fr/home/"
  }
}
```

A missing language path is recorded as skipped rather than failing the entire run.

## Exit behaviour

The command exits with a non-zero status when one or more captures fail. HTTP error pages are still saved and reported as `captured-with-http-error` so broken routes can be reviewed visually.

## Elementor workflow

Use these screenshots as the approval baseline for:

1. Global colours and typography
2. Header and footer sections
3. Homepage reconstruction
4. Reusable child-page templates
5. Desktop, tablet and mobile visual comparison

The intentional exception is the thin red announcement strip on the original homepage, which should not be reproduced in the Elementor build.
