# Palette's Journal - Critical UX/Accessibility Learnings

## 2025-06-08 - Fixed Accessibility Invisibility
**Learning:** In a GitHub profile repository, only `README.md` is rendered on the profile page. Any other markdown files like `wiis.md` remain invisible to visitors. Also, accessibility enhancements like `<span>` with `aria-label` are redundant inside Markdown comments as they are not rendered.
**Action:** Always ensure the primary profile content is in `README.md` and only apply accessibility enhancements to rendered content.
