import { defineMiddleware } from "astro:middleware";
import acceptLanguageParser from "accept-language-parser";
import { defaultLang, languages } from "./i18n/ui";

const supportedLangs = Object.keys(languages);

export const onRequest = defineMiddleware((context, next) => {
	const { request, url, redirect } = context;

	// Only intercept requests to the exact root path
	if (url.pathname === "/") {
		const acceptLanguageHeader = request.headers.get("accept-language");

		let targetLang = defaultLang;

		if (acceptLanguageHeader) {
			// Parse the accept-language header
			const parsedLangs = acceptLanguageParser.parse(acceptLanguageHeader);

			// Find the first language that is supported by our app
			const match = parsedLangs.find((lang) =>
				supportedLangs.includes(lang.code),
			);

			if (match) {
				targetLang = match.code;
			}
		}

		// Perform Edge-level 302 redirect
		return redirect(`/${targetLang}/`, 302);
	}

	return next();
});
