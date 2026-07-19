# Global Header Source Audit

## Status

This document is the implementation contract for recreating the existing TShirtSwiss GitHub Pages header in Elementor Free.

The current GitHub website is the source of truth. The Elementor implementation must preserve the established design and must not replace it with a simplified header.

## Source reviewed

Primary reference:

- `de/home/index.html`

The same header system is expected to be reused across the English, German and French page families, with language-specific labels and URLs.

## Non-negotiable fidelity rule

The Elementor version must preserve, as closely as the WordPress and Elementor Free environment permits:

- section order
- content hierarchy
- desktop and mobile layouts
- navigation depth
- dropdown and drawer interactions
- spacing and proportions
- typography weight and casing
- colours, borders, shadows and radii
- sticky behaviour
- language navigation
- quote call-to-action prominence

No element may be removed merely to make the Elementor implementation easier.

## Existing header architecture

### 1. Preview notice bar

A full-width red notice strip appears above the utility bar.

Required characteristics:

- TShirtSwiss red background
- white uppercase text
- compact 12px presentation
- strong font weight and increased letter spacing
- inner content constrained to the same main wrapper width
- minimum height approximately 38px
- content distributed across the available width
- underlined link treatment where present

### 2. Utility top bar

A black full-width information bar sits between the notice strip and main navigation.

Required characteristics:

- black background
- white text
- subtle translucent lower border
- approximately 48px minimum height
- compact uppercase utility labels
- multiple information items with icon boxes
- red-tinted icon borders and backgrounds
- language links aligned within the same bar on desktop
- centred and evenly spaced utility content

### 3. Main sticky header

The primary white header remains sticky at the top of the viewport after the preceding content scrolls away.

Required characteristics:

- white background
- strong soft shadow beneath the header
- high stacking order
- approximately 108px desktop minimum height
- content constrained to the established wrapper width
- logo at the leading edge
- navigation centred within the remaining space
- quote CTA at the trailing edge

### 4. Brand mark

The current text-based TShirtSwiss mark must be preserved unless an approved image logo is supplied later.

Required characteristics:

- heavy black wordmark
- red accent on the existing highlighted portion
- compact line height
- approximately 34px desktop size
- negative letter spacing consistent with the current source
- small uppercase strapline beneath the wordmark
- strapline approximately 9px with wide letter spacing

### 5. Desktop navigation

The desktop navigation must preserve the full current hierarchy rather than flattening it.

Required characteristics:

- uppercase labels
- heavy font weight
- approximately 12px text
- approximately 25px horizontal gap
- large vertical click and hover area matching the current header height
- dropdown indicator on items with children
- keyboard focus support through `:focus-within` or equivalent accessible behaviour

Expected primary groups include the current site categories, such as:

- Home
- Services
- Products
- Industries
- Resources
- About or company information where present
- Contact or equivalent direct navigation where present

Final labels and destinations must be taken directly from each language version of the existing source during implementation.

### 6. Desktop dropdown menus

Dropdowns are a required part of the design and must not be replaced by simple direct links.

Required characteristics:

- white background
- subtle border
- lower rounded corners
- deep soft shadow
- dropdown positioned directly below the navigation trigger
- initial hidden state using opacity, visibility and vertical translation
- short smooth reveal transition
- left-aligned dropdown text
- hover and keyboard-focus opening behaviour
- red hover colour
- light grey hover background
- internal vertical padding
- support for both single-column and wide two-column menu layouts
- viewport-aware maximum height with scrolling where necessary

Current source dimensions to preserve approximately:

- standard dropdown minimum width: 260px
- services dropdown minimum width: 560px
- wide dropdown minimum width: 620px

### 7. Quote call-to-action

The red quote button is a primary visual and conversion element and must remain prominent.

Required characteristics:

- TShirtSwiss red background
- white uppercase text
- heavy font weight
- compact corner radius
- generous horizontal and vertical padding
- subtle red shadow
- direct link to the correct language-specific quote or contact destination

### 8. Desktop language selector

The language selector must remain visible in the desktop utility area.

Required characteristics:

- English, German and French destinations
- current language visually identifiable
- uppercase compact labels
- heavy white text on the black utility bar
- approximately 10px gap
- no automatic translation dependency; links must point to the corresponding authored language pages

### 9. Mobile header trigger

At the existing responsive breakpoint, the desktop navigation must be replaced with the established mobile control rather than compressed into an unusable row.

Required characteristics:

- black button
- white uppercase label
- compact radius
- menu icon or symbol beside the label
- sufficiently large touch target
- opens the off-canvas mobile panel

### 10. Mobile backdrop

Opening the mobile menu must display a viewport-sized translucent dark backdrop.

Required characteristics:

- fixed positioning across the viewport
- layer beneath the drawer and above page content
- click or tap closes the drawer
- hidden when the drawer is closed

### 11. Mobile off-canvas panel

The existing right-side mobile drawer must be recreated rather than replaced with a basic Elementor dropdown.

Required characteristics:

- fixed to the right side below the mobile header offset
- height extends to the bottom of the viewport
- width capped at approximately 430px and 92vw
- white background
- deep left-facing shadow
- vertical scrolling within the drawer
- overscroll containment
- closed state translated fully off-screen
- short smooth horizontal transition
- body scrolling disabled while open

### 12. Mobile drawer heading

The drawer includes a sticky internal heading row.

Required characteristics:

- white background
- lower divider
- brand text with red accent
- close button at the opposite side
- close button uses black background and white text
- internal heading remains visible while menu content scrolls

### 13. Mobile language selector

The three language links must remain available near the top of the mobile drawer.

Required characteristics:

- centred horizontal arrangement
- uppercase heavy labels
- separated from the menu by a lower border
- correct language-specific destinations

### 14. Mobile navigation accordions

Navigation groups with children must remain expandable on mobile.

Required characteristics:

- semantic expandable controls such as `details/summary`, or an equivalent accessible implementation
- full-width rows
- lower divider between groups
- uppercase heavy parent labels
- plus indicator when closed
- minus indicator when open
- red indicator colour
- nested child links with increased horizontal padding
- grey hover background and red hover text
- direct links remain visually consistent with accordion parent rows

### 15. Mobile quote action

The quote CTA must also appear within the mobile drawer.

Required characteristics:

- red primary button treatment
- centred within the drawer
- appropriate surrounding margin
- correct language-specific destination

## Established visual tokens

The source currently defines these core values:

- red: `#e1111a`
- primary ink: `#111`
- muted text: `#555`
- divider line: `#e7e7e7`
- soft background: `#f7f7f7`
- deep black: `#070707`
- mobile header offset: approximately `84px`
- font stack: `Inter, Arial, Helvetica, sans-serif`
- main content wrapper: `min(1280px, calc(100% - 64px))`

These must be retained unless later source inspection identifies a newer canonical value.

## Elementor Free implementation approach

Because Elementor Free does not provide a complete theme-builder header and mega-menu system, fidelity takes priority over forcing every behaviour into stock widgets.

The preferred implementation is:

1. Native Elementor containers for editable structural regions where practical.
2. Native Elementor widgets for simple text, branding and buttons where they preserve the design.
3. A compact HTML widget for the full navigation hierarchy and interaction hooks where stock widgets cannot reproduce the existing menu accurately.
4. Scoped CSS for the exact desktop, dropdown, sticky and mobile-drawer presentation.
5. Minimal scoped JavaScript for drawer open/close behaviour, backdrop behaviour, Escape-key closing and body scroll locking.
6. Language-specific copies or controlled link maps so EN, DE and FR destinations remain authored and correct.

The use of HTML, CSS or JavaScript is not permission to redesign the component. It is solely a compatibility method for faithfully reproducing the existing source within Elementor Free.

## Responsive verification requirements

Before the header can be marked complete, it must be checked at minimum at:

- 1440px desktop
- 1280px desktop
- 1024px tablet landscape
- 768px tablet portrait
- 430px mobile
- 390px mobile
- 360px mobile

The verification must cover:

- no clipped navigation labels
- no dropdown overflow outside the usable viewport
- correct sticky stacking
- correct drawer offset and width
- usable touch targets
- body scroll lock while the drawer is open
- keyboard navigation and Escape-key closing
- EN, DE and FR link correctness
- preservation of visual proportions from the GitHub source

## Completion gate

The global header is not complete until all of the following are present and verified:

- preview notice bar
- utility top bar and information items
- desktop language selector
- exact wordmark treatment
- full desktop navigation hierarchy
- all dropdown groups
- quote CTA
- sticky behaviour
- mobile trigger
- backdrop
- off-canvas drawer
- sticky drawer heading and close button
- mobile language selector
- expandable mobile menu groups
- mobile quote CTA
- responsive and keyboard behaviour

Any implementation missing one of these items must remain labelled as incomplete and must not be presented as the finished global header.