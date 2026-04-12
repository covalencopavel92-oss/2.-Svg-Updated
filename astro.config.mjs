import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://covalencopavel92-oss.github.io',
  base: '/2.-Svg-Updated',
    
  prefetch: {
    // Removed prefetchAll: true to save bandwidth and speed up initial load
    defaultStrategy: 'hover'
  },
  devToolbar: {
    enabled: false
  }
});
