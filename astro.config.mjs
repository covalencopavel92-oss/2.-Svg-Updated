import db from "@astrojs/db";
import node from "@astrojs/node";
import partytown from "@astrojs/partytown";
import { defineConfig } from "astro/config";

export default defineConfig({
	site: "https://covalencopavel92-oss.github.io",

	prefetch: {
		// Removed prefetchAll: true to save bandwidth and speed up initial load
		defaultStrategy: "hover",
	},

	devToolbar: {
		enabled: true,
	},

	output: "server",

	adapter: node({
		mode: "middleware",
	}),

	integrations: [
		db(),
		partytown({
			config: {
				forward: ["VANTA", "vantaEffect"],
			},
		}),
	],

	i18n: {
		defaultLocale: "en",
		locales: ["en", "ro", "es"],
		routing: {
			prefixDefaultLocale: true,
			redirectToDefaultLocale: true,
		},
	},
});
