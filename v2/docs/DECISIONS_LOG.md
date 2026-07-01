# Decisions Log

This document records approved project decisions.

## Decisions

### D001 - Use GitHub as the v2 source of truth

Date: 2026-07-01

Decision: The existing `albertroe2021-beep/tshirtswiss` repository will hold the TShirtSwiss v2 workspace under the `v2/` folder, developed on a separate branch first.

Reason: Keeps the project version-controlled while avoiding accidental changes to the existing live GitHub Pages site.

Status: Approved

### D002 - HTML before Elementor

Date: 2026-07-01

Decision: The HTML prototype is the master design source. Elementor implementation begins only after the matching HTML page is approved.

Reason: Prevents design drift and ensures Elementor is used as the implementation layer rather than the design decision layer.

Status: Approved

### D003 - Spreadsheet controls SVG mapping

Date: 2026-07-01

Decision: SVG mapping decisions come from the spreadsheet, not from ad hoc repository references.

Reason: Prevents icon mismatches and keeps the icon library auditable.

Status: Approved
