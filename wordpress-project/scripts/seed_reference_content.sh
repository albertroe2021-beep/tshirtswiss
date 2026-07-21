#!/usr/bin/env bash
set -euo pipefail

wp() {
  command wp --allow-root "$@"
}

cd /var/www/html

create_page() {
  local title="$1"
  local slug="$2"
  local parent_id="${3:-0}"
  local page_id

  page_id=$(wp post list --post_type=page --name="$slug" --field=ID --posts_per_page=1)
  if [[ -z "$page_id" ]]; then
    page_id=$(wp post create \
      --post_type=page \
      --post_status=publish \
      --post_title="$title" \
      --post_name="$slug" \
      --post_parent="$parent_id" \
      --porcelain)
  fi

  echo "$page_id"
}

set_elementor_placeholder() {
  local post_id="$1"
  local heading="$2"

  local json
  json='[{"id":"a1b2c3d4","elType":"container","isInner":false,"settings":{"content_width":"boxed","gap":"default"},"elements":[{"id":"h1aa11bb","elType":"widget","widgetType":"heading","settings":{"title":"'"$heading"'","size":"xl"},"elements":[]},{"id":"t1aa11bb","elType":"widget","widgetType":"text-editor","settings":{"editor":"<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ultricies est sed dolor egestas, ut volutpat odio sagittis. Integer posuere consequat tortor, non pretium neque posuere vitae.</p>"},"elements":[]},{"id":"b1aa11bb","elType":"widget","widgetType":"button","settings":{"text":"Lorem Ipsum","link":{"url":"#"},"size":"md"},"elements":[]}]}]'

  wp post meta update "$post_id" _elementor_edit_mode builder >/dev/null
  wp post meta update "$post_id" _elementor_version 4.1.5 >/dev/null
  wp post meta update "$post_id" _elementor_data "$json" >/dev/null
  wp post meta update "$post_id" _elementor_page_settings '[]' >/dev/null
}

create_menu_with_pages() {
  local menu_name="$1"
  shift

  wp menu create "$menu_name" >/dev/null 2>&1 || true

  for page_id in "$@"; do
    wp menu item add-post "$menu_name" "$page_id" >/dev/null 2>&1 || true
  done
}

create_template() {
  local title="$1"
  local template_type="$2"
  local slug="$3"
  local post_id

  post_id=$(wp post list --post_type=elementor_library --name="$slug" --field=ID --posts_per_page=1)
  if [[ -z "$post_id" ]]; then
    post_id=$(wp post create \
      --post_type=elementor_library \
      --post_status=publish \
      --post_title="$title" \
      --post_name="$slug" \
      --porcelain)
  fi

  wp post meta update "$post_id" _elementor_edit_mode builder >/dev/null
  wp post meta update "$post_id" _elementor_version 4.1.5 >/dev/null
  wp post meta update "$post_id" _elementor_template_type "$template_type" >/dev/null
  set_elementor_placeholder "$post_id" "$title"
}

# English pages
EN_HOME=$(create_page "Home" "home")
EN_PRODUCTS=$(create_page "Products" "products")
EN_SERVICES=$(create_page "Services" "services")
EN_INDUSTRIES=$(create_page "Industries" "industries")
EN_RESOURCES=$(create_page "Resources" "resources")
EN_ABOUT=$(create_page "About" "about")
EN_CONTACT=$(create_page "Contact" "contact")
EN_QA=$(create_page "QA" "qa")
EN_BLOG_ARCHIVE=$(create_page "Blog Archive" "blog")
EN_BLOG_POST=$(create_page "Blog Post" "blog-post")

# German pages under /de/
DE_ROOT=$(create_page "Deutsch" "de")
DE_HOME=$(create_page "Home" "de-home" "$DE_ROOT")
DE_PRODUCTS=$(create_page "Products" "de-products" "$DE_ROOT")
DE_SERVICES=$(create_page "Services" "de-services" "$DE_ROOT")
DE_INDUSTRIES=$(create_page "Industries" "de-industries" "$DE_ROOT")
DE_RESOURCES=$(create_page "Resources" "de-resources" "$DE_ROOT")
DE_ABOUT=$(create_page "About" "de-about" "$DE_ROOT")
DE_CONTACT=$(create_page "Contact" "de-contact" "$DE_ROOT")
DE_QA=$(create_page "QA" "de-qa" "$DE_ROOT")
DE_BLOG_ARCHIVE=$(create_page "Blog Archive" "de-blog" "$DE_ROOT")
DE_BLOG_POST=$(create_page "Blog Post" "de-blog-post" "$DE_ROOT")

# French pages under /fr/
FR_ROOT=$(create_page "Français" "fr")
FR_HOME=$(create_page "Home" "fr-home" "$FR_ROOT")
FR_PRODUCTS=$(create_page "Products" "fr-products" "$FR_ROOT")
FR_SERVICES=$(create_page "Services" "fr-services" "$FR_ROOT")
FR_INDUSTRIES=$(create_page "Industries" "fr-industries" "$FR_ROOT")
FR_RESOURCES=$(create_page "Resources" "fr-resources" "$FR_ROOT")
FR_ABOUT=$(create_page "About" "fr-about" "$FR_ROOT")
FR_CONTACT=$(create_page "Contact" "fr-contact" "$FR_ROOT")
FR_QA=$(create_page "QA" "fr-qa" "$FR_ROOT")
FR_BLOG_ARCHIVE=$(create_page "Blog Archive" "fr-blog" "$FR_ROOT")
FR_BLOG_POST=$(create_page "Blog Post" "fr-blog-post" "$FR_ROOT")

# Blog post placeholders per language.
wp post create --post_type=post --post_status=publish --post_title="Blog Post EN" --post_name="blog-post-en" --post_content="Lorem ipsum dolor sit amet, consectetur adipiscing elit." >/dev/null 2>&1 || true
wp post create --post_type=post --post_status=publish --post_title="Blog Post DE" --post_name="blog-post-de" --post_content="Lorem ipsum dolor sit amet, consectetur adipiscing elit." >/dev/null 2>&1 || true
wp post create --post_type=post --post_status=publish --post_title="Blog Post FR" --post_name="blog-post-fr" --post_content="Lorem ipsum dolor sit amet, consectetur adipiscing elit." >/dev/null 2>&1 || true

for page_id in \
  "$EN_HOME" "$EN_PRODUCTS" "$EN_SERVICES" "$EN_INDUSTRIES" "$EN_RESOURCES" "$EN_ABOUT" "$EN_CONTACT" "$EN_QA" "$EN_BLOG_ARCHIVE" "$EN_BLOG_POST" \
  "$DE_HOME" "$DE_PRODUCTS" "$DE_SERVICES" "$DE_INDUSTRIES" "$DE_RESOURCES" "$DE_ABOUT" "$DE_CONTACT" "$DE_QA" "$DE_BLOG_ARCHIVE" "$DE_BLOG_POST" \
  "$FR_HOME" "$FR_PRODUCTS" "$FR_SERVICES" "$FR_INDUSTRIES" "$FR_RESOURCES" "$FR_ABOUT" "$FR_CONTACT" "$FR_QA" "$FR_BLOG_ARCHIVE" "$FR_BLOG_POST"; do
  set_elementor_placeholder "$page_id" "Lorem Ipsum"
done

wp option update show_on_front page
wp option update page_on_front "$EN_HOME"

create_menu_with_pages "Main EN" \
  "$EN_HOME" "$EN_PRODUCTS" "$EN_SERVICES" "$EN_INDUSTRIES" "$EN_RESOURCES" "$EN_ABOUT" "$EN_CONTACT" "$EN_QA" "$EN_BLOG_ARCHIVE" "$EN_BLOG_POST"
create_menu_with_pages "Main DE" \
  "$DE_HOME" "$DE_PRODUCTS" "$DE_SERVICES" "$DE_INDUSTRIES" "$DE_RESOURCES" "$DE_ABOUT" "$DE_CONTACT" "$DE_QA" "$DE_BLOG_ARCHIVE" "$DE_BLOG_POST"
create_menu_with_pages "Main FR" \
  "$FR_HOME" "$FR_PRODUCTS" "$FR_SERVICES" "$FR_INDUSTRIES" "$FR_RESOURCES" "$FR_ABOUT" "$FR_CONTACT" "$FR_QA" "$FR_BLOG_ARCHIVE" "$FR_BLOG_POST"

# Reusable templates for all languages.
for lang in EN DE FR; do
  low_lang=$(echo "$lang" | tr 'A-Z' 'a-z')
  create_template "$lang Header" section "${low_lang}-header"
  create_template "$lang Footer" section "${low_lang}-footer"
  create_template "$lang Product Child" page "${low_lang}-product-child"
  create_template "$lang Service Child" page "${low_lang}-service-child"
  create_template "$lang Industry Child" page "${low_lang}-industry-child"
done

echo "Reference pages, templates, and placeholder Elementor data have been created."
