## 2025-03-05 - Profile Visibility and Emoji Accessibility
**Learning:** In profile-only repositories like siwiis/siwiis, using README.md instead of wiis.md is critical for rendering on GitHub. Additionally, wrapping list emojis in `<span role="img" aria-label="description">` makes them accessible to screen readers without introducing noise to the markdown comments.
**Action:** Ensure the entry point is named README.md and apply the span-wrapping accessibility pattern to visible profile emojis.
