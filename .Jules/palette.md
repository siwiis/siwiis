## 2026-06-25 - Emoji Accessibility in Markdown
**Learning:** Emojis used as bullets or decoration in Markdown are often ignored or misread by screen readers. Wrapping them in `<span role="img" aria-label="description">` ensures they are correctly identified and described.
**Action:** Always wrap non-decorative emojis in semantic HTML tags with ARIA labels when working with Markdown files that serve as primary interfaces (like profile READMEs).
