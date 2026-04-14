import { ui, defaultLang } from './ui';

export function getLangFromUrl(url: URL) {
  const [, lang] = url.pathname.split('/');
  if (lang in ui) return lang as keyof typeof ui;
  return defaultLang;
}

const splitCache: Record<string, string[]> = {};

export function useTranslations(lang: keyof typeof ui) {
  return function t(key: string) {
      let keys = splitCache[key];
      if (!keys) {
          keys = splitCache[key] = key.indexOf('.') === -1 ? [key] : key.split('.');
      }

      let text: any = ui[lang];
      for (const k of keys) {
          if (text && typeof text === 'object' && k in text) {
              text = text[k as keyof typeof text];
          } else {
              // Fallback to default lang if key missing
               let defaultText: any = ui[defaultLang];
               for (const dk of keys) {
                   if (defaultText && typeof defaultText === 'object' && dk in defaultText) {
                       defaultText = defaultText[dk as keyof typeof defaultText];
                   } else {
                       return key;
                   }
               }
               return defaultText;
          }
      }
      return text;
  }
}
