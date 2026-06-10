## 2025-05-22 - Profile README Visibility and Emoji Accessibility
**Learning:** GitHub profile repositories require the filename to be exactly `README.md` to render on the profile page. Additionally, emojis in profile READMEs are often inaccessible to screen readers without proper ARIA markup.
**Action:** Always ensure the profile README is named `README.md` and wrap emojis in `<span role="img" aria-label="...">` to provide context for assistive technology.
