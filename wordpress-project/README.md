# WordPress Project (Elementor Reference Build)

This project provides a reproducible local WordPress environment for building the TShirtSwiss Elementor reference kit.

## Requirements

- Docker
- Docker Compose

## Quick Start

1. Copy env file:

   ```bash
   cp .env.example .env
   ```

2. Start services:

   ```bash
   docker compose up -d
   ```

3. Provision WordPress, theme, and plugins:

   ```bash
   docker compose run --rm wpcli bash /scripts/setup_wordpress.sh
   ```

4. Seed required pages and reusable templates with Elementor placeholders:

   ```bash
   docker compose run --rm wpcli bash /scripts/seed_reference_content.sh
   ```

5. Build export archive:

   ```bash
   docker compose run --rm wpcli bash /scripts/export_reference_kit.sh
   ```

## Installed Components

- WordPress (Docker image `wordpress:6.8.2-php8.2-apache`)
- Theme: `hello-elementor`
- Plugins retained:
  - `elementor` (pinned to `4.1.5`)
  - `litespeed-cache`
  - `wordpress-seo`

## Output

- Export archive path: `exports/tshirtswiss-reference-kit.zip`

## Notes

- This headless setup automates structure and placeholders.
- Final visual parity with the reference HTML must be completed and verified in Elementor Editor UI.
