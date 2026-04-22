## 2026-04-18 - [Contact Form Accessibility & Usability]
**Learning:** Labels that have `pointer-events: none` configured in CSS cannot be interacted with by users (or automated tools like Playwright simulating clicks). Forms should also provide immediate feedback (like disabling buttons) to avoid double submission during simulated or slow network requests.
**Action:** Always ensure labels mapped with `for` attributes do not have `pointer-events: none` applied globally, or override them if they are absolutely positioned but intended to be clicked. Remember to pair visual feedback ('Sending...') with physical constraints (`disabled=true`) on forms.
## 2024-05-19 - Adding Focus Visible Styles
**Learning:** Added global `:focus-visible` styles for `a`, `button`, `input`, `textarea`, `select`, and custom interactive elements using `[tabindex]:not([tabindex="-1"])`. This improves keyboard accessibility without cluttering mouse user experience.
**Action:** Always add custom global `:focus-visible` styles if none exist, as browsers often have varied defaults or remove outlines universally by mistake.
## $(date +%Y-%m-%d) - Adding ARIA Stateful Attributes to Interactive Elements
**Learning:** When turning generic `div` elements into interactive elements (like the language switcher) or making existing buttons toggle states (like the hamburger menu or lock button) in Astro components with View Transitions, standard HTML roles and `tabindex` aren't enough. The ARIA state attributes (`aria-expanded`, `aria-pressed`) must be explicitly toggled in the vanilla JS `<script>` logic alongside the CSS classes. Keyboard event listeners (Space/Enter) must also be manually attached to custom elements to maintain accessibility.
**Action:** When adding or fixing accessibility for interactive components, explicitly check the JavaScript to ensure ARIA states dynamically match the visual/functional state of the element during user interaction, and manually add keyboard handlers for non-native interactive elements.
## 2025-02-12 - Explicit focus styles for sidebar icons

**Learning:** When using visually hidden text for icons in collapsed sidebar states, native focus indicators (like tab rings) often look misaligned or are completely missing because the width changes dramatically on hover/expand.

**Action:** Ensure that buttons/interactive elements have explicit focus styles applied specifically for `focus-visible`.
## $(date +%Y-%m-%d) - Interactive Labels and Hit Areas
**Learning:** Applying `pointer-events: none` to `label` elements globally is detrimental to accessibility, as it prevents users from clicking the label to focus its associated input. Furthermore, using `type="search"` instead of `type="text"` provides built-in browser features like the clear (x) button.
**Action:** Avoid `pointer-events: none` on `<label>` elements unless there is a specific, well-handled reason. Ensure visual wrappers for inputs delegate clicks to the actual input field to maximize the interactive hit area.
