#!/usr/bin/env bash
set -euo pipefail

wp() {
  command wp --allow-root "$@"
}

cd /var/www/html

wait_for_db() {
  local attempts=0
  until wp db query 'SELECT 1;' --skip-column-names >/dev/null 2>&1; do
    attempts=$((attempts + 1))
    if [[ $attempts -gt 40 ]]; then
      echo "Database connection failed after multiple retries." >&2
      exit 1
    fi
    echo "Waiting for database... ($attempts/40)"
    sleep 3
  done
}

if [[ ! -f wp-includes/version.php ]]; then
  wp core download --locale=en_US --force
fi

if [[ ! -f wp-config.php ]]; then
  wp config create \
    --dbname="$WORDPRESS_DB_NAME" \
    --dbuser="$WORDPRESS_DB_USER" \
    --dbpass="$WORDPRESS_DB_PASSWORD" \
    --dbhost="$WORDPRESS_DB_HOST" \
    --skip-check
fi

wait_for_db

if ! wp core is-installed >/dev/null 2>&1; then
  wp core install \
    --url="$WP_HOME_URL" \
    --title="TShirtSwiss Reference Kit" \
    --admin_user="$WP_ADMIN_USER" \
    --admin_password="$WP_ADMIN_PASSWORD" \
    --admin_email="$WP_ADMIN_EMAIL"
fi

# Remove default content that is not part of the reference kit.
wp post delete 1 2 3 --force >/dev/null 2>&1 || true

wp option update blogdescription "Elementor Reference Build"
wp rewrite structure '/%postname%/' --hard
wp rewrite flush --hard

# Keep only required plugins.
wp plugin install elementor --version=4.1.5 --activate
wp plugin install litespeed-cache --activate
wp plugin install wordpress-seo --activate

for plugin in $(wp plugin list --field=name); do
  case "$plugin" in
    elementor|litespeed-cache|wordpress-seo)
      ;;
    *)
      wp plugin deactivate "$plugin" --quiet || true
      wp plugin delete "$plugin" --quiet || true
      ;;
  esac
done

wp theme install hello-elementor --activate
for theme in $(wp theme list --field=name); do
  if [[ "$theme" != "hello-elementor" ]]; then
    wp theme delete "$theme" --quiet || true
  fi
done

# Elementor experiments requested in spec.
for flag in container nested-elements nested-accordion nested-tabs nested-carousel editor-v4; do
  wp option update "elementor_experiment-${flag}" active >/dev/null 2>&1 || true
done

# Baseline Elementor site settings.
wp option update elementor_container_width 1200 >/dev/null 2>&1 || true
wp option update elementor_viewport_lg 1025 >/dev/null 2>&1 || true
wp option update elementor_viewport_md 768 >/dev/null 2>&1 || true

echo "WordPress core, theme, and required plugins are configured."
