# Manual SVG Update Progress

This tracker records the section-by-section SVG icon standardisation work based on:

- `SVG number to phrase(2).xlsx`
- `docs/svg-icon-mapping-draft.md`
- the committed SVG files from `New_SVG_Files_30_06_2026`

## Current decision

The broad automatic replacement engine was tested and rejected because it matched nearby phrases too broadly and placed icons in the wrong areas.

From this point onward, updates must be made section-by-section with explicit placement only.

## Verified homepage mappings

| Page | Section | Phrase | Ref# | SVG file | Status |
|---|---|---|---:|---|---|
| Home | Top bar | Swiss Managed | 1 | shield-with-cross-svgrepo-com (1).svg | Applied |
| Home | Top bar | Factory in Thailand | 2 | factory-building-svgrepo-com.svg | Applied |
| Home | Top bar | Premium Quality | 3 | quality-5-svgrepo-com.svg | Applied |
| Home | Top bar | Worldwide Shipping | 6 | plane-svgrepo-com (1).svg | Applied |
| Home | Trust cards | Swiss Quality Standards | 1 | shield-with-cross-svgrepo-com (1).svg | Applied |
| Home | Trust cards | Factory Direct Pricing | 2 | factory-building-svgrepo-com.svg | Applied |
| Home | Trust cards | Strict Quality Control | 4 | quality-5-svgrepo-com.svg | Applied |
| Home | Trust cards | Worldwide Shipping | 6 | plane-svgrepo-com (1).svg | Applied |
| Home | Trust cards | Long Term Partner | 8 | handshake-svgrepo-com.svg | Applied |
| Home | Process | Consultation | 10 | speech-bubbles-conversation-svgrepo-com (1).svg | Applied |
| Home | Process | Sample & Approval | 16 | review-checkmark-svgrepo-com.svg | Applied |
| Home | Process | Production | 2 | factory-building-svgrepo-com.svg | Applied |
| Home | Process | Quality Check | 5 | quality-5-svgrepo-com.svg | Applied |
| Home | Process | Packing & Shipping | 6 | plane-svgrepo-com (1).svg | Applied |

## Next manual sections

| Order | Page / Section | Status | Notes |
|---:|---|---|---|
| 1 | Home top bar | Completed | Explicit mapping verified. |
| 2 | Home trust cards | Completed | Explicit mapping verified. |
| 3 | Home process cards | Completed | Explicit mapping verified. |
| 4 | Home product cards | In progress | Needs final phrase-by-phrase check against spreadsheet. |
| 5 | Home industry cards | Pending | Do not infer. Use only exact spreadsheet rows. |
| 6 | Product pages | Pending | Convert one page at a time. |
| 7 | Industry pages | Pending | Convert one page at a time. |
| 8 | Service pages | Pending | Convert one page at a time. |
| 9 | Resources / Contact / Quote | Pending | Convert after page groups above. |

## Manual update rules

1. Do not run the broad regex replacement script against the whole site.
2. Do not infer mappings from nearby text.
3. Only place an SVG where the section has an explicit spreadsheet phrase and Ref#.
4. Add `data-ref` to every placed icon so visual review is easier.
5. Keep legacy inline SVGs removed from completed sections.
6. Commit one page or one section at a time.
