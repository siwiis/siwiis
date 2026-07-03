## 2026-07-03 - Emoji Accessibility in Markdown
**Learning:** Emojis in Markdown or static HTML files are often not accessible to screen readers, which may skip them or read them incorrectly.
**Action:** Wrap emojis in `<span role="img" aria-label="description">...</span>` to provide a meaningful text alternative and ensure screen-reader accessibility.
