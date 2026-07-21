## 2025-01-20 - Profile Emoji Accessibility
**Learning:** Wrapping profile emojis in Markdown with `<span role="img" aria-label="description">...</span>` ensures they are accessible to screen readers, while avoiding modifying emojis in HTML/Markdown comments minimizes PR noise.
**Action:** Always verify the standard profile emojis and their hex code mappings to write precise aria-labels, and preserve comment blocks untouched.
