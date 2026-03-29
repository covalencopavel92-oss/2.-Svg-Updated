// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  prefetch: {
    prefetchAll: true, // Forces all links to prefetch
    defaultStrategy: 'hover'
  },
  devToolbar: {
    enabled: false
  }
});
