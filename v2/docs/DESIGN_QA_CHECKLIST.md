# TShirtSwiss v2 Design QA Checklist

## Purpose

This checklist is the mandatory page-level quality gate for the approved HTML prototype and later WordPress Elementor implementation.

A page is not complete until every applicable item has been checked, exceptions have been documented, and the final sign-off section has been completed.

## Status key

- `[ ]` Not checked
- `[x]` Passed
- `N/A` Not applicable
- `Blocked` Cannot be completed until a dependency is resolved

---

# 1. Page Identity and Scope

- [ ] Page title matches the approved page inventory.
- [ ] Repository path and public URL are correct.
- [ ] Page purpose is clear within the first viewport.
- [ ] Page belongs to the correct navigation group.
- [ ] Breadcrumbs, where used, reflect the correct hierarchy.
- [ ] No unapproved sections have been added.
- [ ] Approved page structure has not been overwritten.
- [ ] Any deviations from the page template are documented.

# 2. Brand Consistency

- [ ] Approved TShirtSwiss red, black, white and neutral colours are used consistently.
- [ ] Typography follows the approved design system.
- [ ] Font sizes, weights and line heights match equivalent sections elsewhere.
- [ ] Buttons follow approved primary, secondary and outline styles.
- [ ] Border radii are consistent.
- [ ] Shadows are consistent and restrained.
- [ ] Section spacing follows the approved spacing system.
- [ ] Cards use consistent padding, borders and hover behaviour.
- [ ] Icons match the approved SVG reference library.
- [ ] No emoji or unrelated icon style is used in place of approved icons.
- [ ] Logo treatment is consistent in header, footer and mobile navigation.

# 3. Header and Navigation

- [ ] Header matches the approved global header structure.
- [ ] Desktop navigation contains all approved top-level items.
- [ ] Mega-menu groupings match the navigation map.
- [ ] All menu links point to the correct page.
- [ ] Current page state is clear where applicable.
- [ ] Request a Quote remains visually prominent.
- [ ] Mobile menu opens and closes correctly.
- [ ] Mobile menu exposes every approved child page.
- [ ] Mobile menu does not trap scrolling incorrectly.
- [ ] Escape key and close controls work where applicable.
- [ ] Keyboard focus moves logically through navigation items.
- [ ] Sticky header does not cover anchored content.

# 4. Hero Section

- [ ] Hero clearly communicates the page topic.
- [ ] One H1 is present.
- [ ] H1 is concise, specific and unique to the page.
- [ ] Supporting copy explains the page value proposition.
- [ ] Primary CTA is visible above the fold where appropriate.
- [ ] Secondary CTA is relevant and not competing unnecessarily.
- [ ] Hero image matches the exact page subject.
- [ ] Hero image provides adequate text-safe space.
- [ ] Text contrast remains readable across the full crop.
- [ ] Hero height is appropriate on desktop, tablet and mobile.
- [ ] Mobile crop preserves the subject and intended meaning.
- [ ] Hero does not contain unnecessary decorative clutter.
- [ ] Any hero form is usable and does not overwhelm the content.

# 5. Image Relevance and Quality

- [ ] Every image supports its adjacent heading and copy.
- [ ] Product pages show the exact product.
- [ ] Industry pages show the relevant people wearing the relevant apparel.
- [ ] Service pages show the actual process, machinery, material or production action.
- [ ] Generic office meetings, unrelated factories and empty environments have been removed.
- [ ] The same hero image is not reused on another page.
- [ ] Supporting-image reuse is intentional and documented.
- [ ] Image source and licence are recorded.
- [ ] Image resolution is sufficient for the rendered size.
- [ ] Images are not stretched or distorted.
- [ ] Desktop crop is approved.
- [ ] Tablet crop is approved.
- [ ] Mobile crop is approved.
- [ ] Important faces, logos and garment details remain visible.
- [ ] Image colour treatment matches the photography style guide.
- [ ] No visible stock watermark, compression damage or AI artefacts are present.

# 6. Image Technical Requirements

- [ ] Descriptive lowercase filename is used.
- [ ] AVIF or WebP version is available.
- [ ] JPG fallback is included where required.
- [ ] Intrinsic width and height are defined.
- [ ] Responsive image behaviour is configured.
- [ ] `srcset` or Elementor responsive image output is correct.
- [ ] Above-the-fold hero loading is prioritised appropriately.
- [ ] Below-the-fold images use lazy loading.
- [ ] Images are compressed without visible quality loss.
- [ ] Mobile devices do not download unnecessarily large desktop files.
- [ ] Decorative background images are handled accessibly.
- [ ] No image causes cumulative layout shift.

# 7. Content Quality

- [ ] Copy is grammatically correct.
- [ ] Spelling follows the approved English variant.
- [ ] Tone matches the Content Style Guide.
- [ ] No placeholder or generator text remains.
- [ ] No duplicated paragraphs appear unintentionally.
- [ ] Claims about quality, production, locations and shipping are accurate.
- [ ] Benefits are explained before excessive technical detail.
- [ ] Page-specific terminology is used consistently.
- [ ] Headings are descriptive rather than generic.
- [ ] Paragraph lengths remain readable.
- [ ] Lists are used only where they improve comprehension.
- [ ] CTA wording is consistent with the intended action.
- [ ] Contact details are accurate.
- [ ] Any pricing, turnaround or MOQ statements are verified.

# 8. Heading Structure

- [ ] Exactly one H1 is present.
- [ ] H2 headings divide the main page sections logically.
- [ ] H3 headings are nested under the correct H2.
- [ ] Heading levels are not skipped for visual styling.
- [ ] Heading text is unique and meaningful.
- [ ] Decorative text is not incorrectly marked as a heading.

# 9. Layout and Alignment

- [ ] Main content width matches the approved container system.
- [ ] Section padding is consistent.
- [ ] Grid columns align correctly.
- [ ] Cards have consistent heights where intended.
- [ ] Card content aligns predictably.
- [ ] Images align with adjacent content.
- [ ] Buttons align consistently within repeated components.
- [ ] No text or image overlaps occur.
- [ ] No content overflows its container.
- [ ] No unintended horizontal scrolling occurs.
- [ ] Whitespace supports hierarchy without appearing excessive.
- [ ] Sections are not cramped on smaller screens.
- [ ] Long words, URLs and headings wrap correctly.

# 10. Reusable Components

- [ ] Trust bar matches the approved component.
- [ ] Product cards match the approved component.
- [ ] Industry cards match the approved component.
- [ ] Service cards match the approved component.
- [ ] Process steps use consistent numbering and spacing.
- [ ] FAQ components behave consistently.
- [ ] Testimonial or case-study cards use consistent attribution.
- [ ] CTA bands use consistent typography, spacing and button styles.
- [ ] Global footer matches the approved footer structure.
- [ ] Component changes are reflected in the Design Bible where necessary.

# 11. Forms

- [ ] Every field has a visible or programmatically associated label.
- [ ] Required fields are clearly identified.
- [ ] Input types are appropriate.
- [ ] Placeholder text does not replace labels.
- [ ] Keyboard navigation follows the intended order.
- [ ] Focus styles are visible.
- [ ] Validation messages are clear and specific.
- [ ] Error messages remain visible near the affected field.
- [ ] Success state is clear.
- [ ] Form submission destination is correct.
- [ ] Spam protection is configured where required.
- [ ] Privacy consent wording is present where required.
- [ ] Mobile input keyboards match the field type.
- [ ] Form controls are large enough for touch use.
- [ ] Form layout works at 390 px width.

# 12. Calls to Action and Conversion

- [ ] Primary CTA is clear and visible.
- [ ] CTA destination matches the wording.
- [ ] Secondary CTA supports rather than distracts from the main action.
- [ ] Quote pathway is easy to find.
- [ ] Contact options are obvious.
- [ ] Trust signals appear near high-intent actions where useful.
- [ ] Benefits are visible before the final CTA.
- [ ] CTA text uses action-oriented wording.
- [ ] Repeated CTAs remain consistent.
- [ ] No dead-end section exists without a logical next action.

# 13. Accessibility

- [ ] Page language is defined.
- [ ] Heading hierarchy is correct.
- [ ] Landmark regions are used appropriately.
- [ ] Keyboard navigation reaches all interactive elements.
- [ ] Focus order is logical.
- [ ] Focus indicators are clearly visible.
- [ ] Colour contrast meets WCAG AA requirements.
- [ ] Informative images have accurate alt text.
- [ ] Decorative images use empty alt text or equivalent treatment.
- [ ] Icon-only controls have accessible names.
- [ ] Links make sense out of context.
- [ ] Buttons are implemented as buttons where appropriate.
- [ ] Form errors are announced accessibly.
- [ ] Touch targets are at least 44 by 44 CSS pixels where practical.
- [ ] Motion respects reduced-motion preferences.
- [ ] Content remains usable at 200% zoom.

# 14. Responsive QA

## Desktop

- [ ] Checked at 1440 px width.
- [ ] Checked at 1280 px width.
- [ ] Navigation, grids and hero composition remain balanced.
- [ ] No oversized empty areas appear.

## Tablet

- [ ] Checked at 1024 px width.
- [ ] Checked at 768 px width.
- [ ] Columns stack or resize predictably.
- [ ] Navigation transition behaves correctly.
- [ ] Image crops remain meaningful.

## Mobile

- [ ] Checked at 430 px width.
- [ ] Checked at 390 px width.
- [ ] Checked at 360 px width where practical.
- [ ] No horizontal scrolling occurs.
- [ ] Header and mobile menu function correctly.
- [ ] Hero content remains legible.
- [ ] Buttons are easy to tap.
- [ ] Cards stack in the intended order.
- [ ] Tables are scrollable or transformed appropriately.
- [ ] Images preserve the intended subject.
- [ ] Forms remain usable.
- [ ] Sticky elements do not obscure content.

# 15. Performance

- [ ] No unnecessary third-party scripts are loaded.
- [ ] CSS and JavaScript are limited to what the page requires.
- [ ] Images are optimised.
- [ ] Fonts are optimised and loaded efficiently.
- [ ] Hero media does not delay the main content unnecessarily.
- [ ] Layout shift is controlled.
- [ ] Offscreen media is lazy loaded.
- [ ] No broken asset requests appear in the browser console.
- [ ] No duplicate libraries are loaded.
- [ ] Page remains usable on a slower mobile connection.
- [ ] Lighthouse performance issues have been reviewed.
- [ ] Core Web Vitals risks are documented.

# 16. SEO

- [ ] Page title is unique and accurate.
- [ ] Meta description is unique and useful.
- [ ] Canonical URL is correct.
- [ ] One H1 is present.
- [ ] Heading structure is logical.
- [ ] Main topic appears naturally in the content.
- [ ] Image alt text is descriptive and not keyword stuffed.
- [ ] Internal links point to relevant pages.
- [ ] Anchor text is descriptive.
- [ ] Open Graph title, description and image are appropriate.
- [ ] Twitter/social preview data is appropriate where used.
- [ ] Structured data is valid where applicable.
- [ ] Indexing directives are correct.
- [ ] No broken links are present.
- [ ] Redirect requirements are documented before migration.

# 17. Links and Functional Checks

- [ ] Header links work.
- [ ] Footer links work.
- [ ] CTA links work.
- [ ] Breadcrumb links work.
- [ ] Card links work.
- [ ] Contact links use correct telephone and email formats.
- [ ] External links open as intended.
- [ ] Download links point to the correct files.
- [ ] Language-switcher links point to the correct equivalent page.
- [ ] No link points to an outdated preview path unintentionally.
- [ ] No JavaScript console errors are present.

# 18. Footer

- [ ] Footer structure matches the approved global footer.
- [ ] Footer navigation is complete.
- [ ] Contact information is correct.
- [ ] Legal and privacy links are present where required.
- [ ] Copyright year and business name are correct.
- [ ] Footer remains readable on mobile.
- [ ] Footer icons match the SVG library.
- [ ] No obsolete links remain.

# 19. Elementor Migration Readiness

- [ ] Page sections can be reproduced with Elementor containers.
- [ ] Global styles are identified.
- [ ] Reusable components are identified as templates or global widgets.
- [ ] Header and footer dependencies are documented.
- [ ] Dynamic content requirements are identified.
- [ ] Form integrations are documented.
- [ ] Responsive behaviour can be reproduced without custom hacks where practical.
- [ ] Asset paths are ready for WordPress media migration.
- [ ] URL changes from `/pages/` to WordPress paths are documented.
- [ ] No normal content update requires editing generated code.

# 20. Final Page Sign-Off

| Sign-off area | Reviewer | Date | Result | Notes |
|---|---|---|---|---|
| Design | Pending | Pending | Pending | |
| Content | Pending | Pending | Pending | |
| Images | Pending | Pending | Pending | |
| Responsive | Pending | Pending | Pending | |
| Accessibility | Pending | Pending | Pending | |
| Performance | Pending | Pending | Pending | |
| SEO | Pending | Pending | Pending | |
| Functional QA | Pending | Pending | Pending | |
| Elementor readiness | Pending | Pending | Pending | |

## Final status

- [ ] Approved HTML master
- [ ] Approved for Elementor implementation
- [ ] Approved and locked

## Exceptions and deferred items

Record every known exception, dependency or deferred improvement here.

| Item | Reason | Owner | Target phase | Status |
|---|---|---|---|---|
| None recorded | — | — | — | — |

## Lock rule

Once a page is marked `Approved and locked`, any later change must:

1. Be recorded in the Decisions Log or Change Log.
2. Identify the affected component or section.
3. Reopen the relevant QA items.
4. Repeat responsive, accessibility and functional checks.
5. Receive approval before the master page is updated.
