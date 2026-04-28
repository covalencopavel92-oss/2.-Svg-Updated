## 2023-10-27 - Dynamic Content Announcement in Quizzes and Forms
**Learning:** Screen readers miss dynamic state changes like new quiz questions replacing old ones, or success messages appearing after async form submissions, unless explicitly told to announce them.
**Action:** Always add `aria-live="polite"` (and `role="status"` where appropriate) to containers where text content is dynamically replaced via JavaScript, ensuring screen reader users are informed of the updates.
