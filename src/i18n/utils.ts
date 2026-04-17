import { defaultLang, type UIKeys, ui } from "./ui";

export function getLangFromUrl(url: URL) {
	const [, lang] = url.pathname.split("/");
	if (lang in ui) return lang as keyof typeof ui;
	return defaultLang;
}

export function useTranslations(lang: keyof typeof ui) {
	return function t(key: UIKeys) {
		if (key in ui[lang]) {
			return ui[lang][key];
		}
		return ui[defaultLang][key] || key;
	};
}
