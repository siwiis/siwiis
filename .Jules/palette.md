## 2025-01-24 - Accessible Emoji Pattern
**Learning:** Wrapping emojis in `<span role="img" aria-label="...">...</span>` in GitHub profile READMEs provides crucial context for screen reader users and is a safe, high-impact micro-UX improvement for documentation-heavy repositories.
**Action:** Always check for raw emojis in Markdown files and apply this accessible wrapping pattern to ensure semantic clarity.

## 2025-01-24 - Profile Visibility UX
**Learning:** In GitHub profile repositories (e.g., `user/user`), the entry point must be named `README.md` for it to render on the profile page. Using other names like `wiis.md` prevents the UX intended for this "special" repository type.
**Action:** Verify the filename of profile entry points and ensure they match the platform's expected `README.md` convention.
