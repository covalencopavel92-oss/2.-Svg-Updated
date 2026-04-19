## 2026-04-18 - [Contact Form Accessibility & Usability]
**Learning:** Labels that have `pointer-events: none` configured in CSS cannot be interacted with by users (or automated tools like Playwright simulating clicks). Forms should also provide immediate feedback (like disabling buttons) to avoid double submission during simulated or slow network requests.
**Action:** Always ensure labels mapped with `for` attributes do not have `pointer-events: none` applied globally, or override them if they are absolutely positioned but intended to be clicked. Remember to pair visual feedback ('Sending...') with physical constraints (`disabled=true`) on forms.
## 2024-05-19 - Adding Focus Visible Styles
**Learning:** Added global `:focus-visible` styles for `a`, `button`, `input`, `textarea`, `select`, and custom interactive elements using `[tabindex]:not([tabindex="-1"])`. This improves keyboard accessibility without cluttering mouse user experience.
**Action:** Always add custom global `:focus-visible` styles if none exist, as browsers often have varied defaults or remove outlines universally by mistake.
