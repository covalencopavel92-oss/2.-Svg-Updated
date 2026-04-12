import { defineConfig } from 'astro/config';

export default defineConfig({

  site: 'https://[your-username].github.io',
  base: '/[repository-name]',
    
  prefetch: {
    // Removed prefetchAll: true to save bandwidth and speed up initial load
    defaultStrategy: 'hover'
  },
  devToolbar: {
    enabled: false
  }
});
