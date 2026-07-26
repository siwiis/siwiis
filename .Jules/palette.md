## 2024-07-26 - Markdown Emoji Wrapping and Profile Naming Conventions
**Learning:** Raw emojis in profile Markdown documents must never be wrapped in HTML span tags (such as <span role='img'>) as it degrades source file readability and modern screen readers support raw emojis natively. Additionally, for a user's GitHub profile to render correctly, the file must be named `README.md` rather than a custom file name like `wiis.md`.
**Action:** Keep emojis raw and unwrapped in Markdown files and ensure the repository's profile entry point is exactly `README.md`.
