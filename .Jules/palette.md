## 2026-06-28 - Profile Visibility and Emoji Accessibility
**Learning:** For GitHub profile repositories, the content must be in `README.md` to be visible. Additionally, emojis in Markdown are not accessible by default; wrapping them in a `span` with `role="img"` and an `aria-label` ensures they are correctly interpreted by screen readers.
**Action:** Always verify that profile repositories use `README.md` and ensure all emojis are wrapped in accessible spans.
