import { defineConfig } from 'astro/config';

export default defineConfig({
  prefetch: {
    // Removed prefetchAll: true to save bandwidth and speed up initial load
    defaultStrategy: 'hover'
  },
  devToolbar: {
    enabled: false
  }
});
