## 2024-10-27 - Parallel Network Requests with Guaranteed Execution Order
**Learning:** Loading dependent third-party scripts sequentially (e.g. `vanta.js` waiting for `three.js`) creates a performance bottleneck through a network waterfall.
**Action:** When injecting dependent client scripts, fetch them simultaneously via `Promise.all` but set `script.async = false` on the injected DOM elements. This leverages HTML5 spec behavior to download them in parallel while strictly guaranteeing they execute in DOM insertion order, ensuring dependencies run first without race conditions.
