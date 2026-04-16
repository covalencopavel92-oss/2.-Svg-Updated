import json

ui_content = {
    "en": {
        "nav": { "home": "Home", "consultancy": "Consultancy", "services": "Services", "reviews": "Reviews", "blog": "Blog", "contact": "Contact", "theme": "Theme" },
        "home": {
            "subtitle": "Business Digitalization Consultancy & Digital Marketing Services",
            "desc": "At Scale Automata, we engineer digital growth. By fusing advanced data analytics, high-conversion web development, and targeted omnichannel marketing, we transform traditional workflows into scalable, future-proof digital ecosystems. From deep technical SEO audits to full-scale enterprise digitalization roadmaps, we build the frameworks that turn your business into an industry leader.",
            "explore": "Explore Services",
            "assessment": "Take Assessment"
        },
        "consult": { "title": "Consultancy & Audits", "subtitle": "Discover the right path to digital excellence for your business." },
        "services": { "title": "Our Services", "subtitle": "Data-driven solutions to elevate your digital presence." },
        "reviews": { "title": "Client Testimonials", "subtitle": "See what businesses are saying about our transformative services." },
        "blog": { "title": "Insights & Strategy", "subtitle": "Latest thoughts on digitalization, marketing trends, and business growth." },
        "contact": { "title": "Let's Talk Growth", "subtitle": "Reach out to discuss how Scale Automata can transform your digital ecosystem.", "name": "Full Name", "email": "Email Address", "subject": "Subject", "message": "Your Message", "send": "Send Message", "success": "Message sent successfully! We will get back to you within 24 hours." },
        "contactDetails": { "address": "Address", "phone": "Phone number", "whatsapp": "WhatsApp", "email": "Email" },
        "footer": { "privacy": "Privacy Policy", "terms": "Terms & Conditions" }
    },
    "ro": {
        "nav": { "home": "Acasă", "consultancy": "Consultanță", "services": "Servicii", "reviews": "Recenzii", "blog": "Blog", "contact": "Contact", "theme": "Temă" },
        "home": {
            "subtitle": "Consultanță în Digitalizarea Afacerilor și Servicii de Marketing Digital",
            "desc": "La Scale Automata, proiectăm creșterea digitală. Prin fuzionarea analizei avansate de date, dezvoltării web cu conversie ridicată și marketingului omnichannel direcționat, transformăm fluxurile de lucru tradiționale în ecosisteme digitale scalabile și pregătite pentru viitor. De la audituri SEO tehnice profunde până la foi de parcurs complete pentru digitalizarea companiilor, construim cadrele care transformă afacerea dvs. într-un lider al industriei.",
            "explore": "Explorează Serviciile",
            "assessment": "Fă o Evaluare"
        },
        "consult": { "title": "Consultanță și Audituri", "subtitle": "Descoperă calea potrivită către excelența digitală pentru afacerea ta." },
        "services": { "title": "Serviciile Noastre", "subtitle": "Soluții bazate pe date pentru a-ți ridica prezența digitală." },
        "reviews": { "title": "Testimoniale Clienți", "subtitle": "Vezi ce spun alte companii despre serviciile noastre transformatoare." },
        "blog": { "title": "Perspective și Strategie", "subtitle": "Cele mai noi gânduri despre digitalizare, tendințe de marketing și creșterea afacerilor." },
        "contact": { "title": "Să Discutăm despre Creștere", "subtitle": "Contactează-ne pentru a discuta cum Scale Automata îți poate transforma ecosistemul digital.", "name": "Nume Complet", "email": "Adresă de Email", "subject": "Subiect", "message": "Mesajul Tău", "send": "Trimite Mesajul", "success": "Mesajul a fost trimis cu succes! Vom reveni cu un răspuns în maxim 24 de ore." },
        "contactDetails": { "address": "Adresă", "phone": "Număr de telefon", "whatsapp": "WhatsApp", "email": "Email" },
        "footer": { "privacy": "Politica de Confidențialitate", "terms": "Termeni și Condiții" }
    },
    "es": {
        "nav": { "home": "Inicio", "consultancy": "Consultoría", "services": "Servicios", "reviews": "Reseñas", "blog": "Blog", "contact": "Contacto", "theme": "Tema" },
        "home": {
            "subtitle": "Consultoría en Digitalización de Empresas y Servicios de Marketing Digital",
            "desc": "En Scale Automata, diseñamos el crecimiento digital. Al fusionar análisis de datos avanzados, desarrollo web de alta conversión y marketing omnicanal dirigido, transformamos los flujos de trabajo tradicionales en ecosistemas digitales escalables y preparados para el futuro. Desde profundas auditorías técnicas de SEO hasta hojas de ruta de digitalización empresarial a gran escala, construimos los marcos que convierten su negocio en un líder de la industria.",
            "explore": "Explorar Servicios",
            "assessment": "Hacer Evaluación"
        },
        "consult": { "title": "Consultoría y Auditorías", "subtitle": "Descubre el camino correcto hacia la excelencia digital para tu negocio." },
        "services": { "title": "Nuestros Servicios", "subtitle": "Soluciones basadas en datos para elevar tu presencia digital." },
        "reviews": { "title": "Testimonios de Clientes", "subtitle": "Mira lo que dicen las empresas sobre nuestros servicios transformadores." },
        "blog": { "title": "Perspectivas y Estrategia", "subtitle": "Últimos pensamientos sobre digitalización, tendencias de marketing y crecimiento empresarial." },
        "contact": { "title": "Hablemos de Crecimiento", "subtitle": "Comunícate para discutir cómo Scale Automata puede transformar tu ecosistema digital.", "name": "Nombre Completo", "email": "Correo Electrónico", "subject": "Asunto", "message": "Tu Mensaje", "send": "Enviar Mensaje", "success": "¡Mensaje enviado con éxito! Nos pondremos en contacto contigo en 24 horas." },
        "contactDetails": { "address": "Dirección", "phone": "Número de teléfono", "whatsapp": "WhatsApp", "email": "Correo electrónico" },
        "footer": { "privacy": "Política de Privacidad", "terms": "Términos y Condiciones" }
    }
}

def flatten(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

new_ui = {}
for lang, content in ui_content.items():
    new_ui[lang] = flatten(content)

print("export const languages = {")
print("  en: 'English',")
print("  ro: 'Română',")
print("  es: 'Español',")
print("};")
print("")
print("export const defaultLang = 'en';")
print("")
print("export const ui = {")
for lang, content in new_ui.items():
    print(f"    {lang}: {{")
    for k, v in content.items():
        print(f"        '{k}': {repr(v)},")
    print("    },")
print("} as const;")
print("")
print("export type UILang = typeof defaultLang;")
print("export type UIKeys = keyof typeof ui[UILang];")
