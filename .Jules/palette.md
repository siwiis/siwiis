## 2025-02-15 - Accessible Profile Emojis
**Learning:** Wrapping emojis in `<span role="img" aria-label="...">` ensures that screen readers can correctly announce them, enhancing the accessibility of GitHub profile READMEs.
**Action:** Always wrap profile emojis with standard ARIA role/label spans while preserving the raw text for visual users and keeping comments untouched.
