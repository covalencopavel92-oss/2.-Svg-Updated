import codecs
import re

# Fix Sidebar.astro
sidebar_path = 'src/components/Sidebar.astro'
with open(sidebar_path, 'r') as f:
    sidebar_content = f.read()

sidebar_content = sidebar_content.replace('href="tel:{t(\'sidebar.phone\')}"', 'href={`tel:${t(\'sidebar.phone\')}`}')
sidebar_content = sidebar_content.replace('placeholder="{t(\'sidebar.search\')}"', 'placeholder={t(\'sidebar.search\')}')
sidebar_content = sidebar_content.replace('aria-label="{t(\'sidebar.lock\')}"', 'aria-label={t(\'sidebar.lock\')}')

with open(sidebar_path, 'w') as f:
    f.write(sidebar_content)


# Fix ppc-and-social-ads.astro title
ppc_path = 'src/pages/[lang]/services/ppc-and-social-ads.astro'
with open(ppc_path, 'r') as f:
    ppc_content = f.read()

# I didn't actually change title in ppc but let's check it
ppc_content = ppc_content.replace('<Layout title="Google & Social Ads | Scale Automata">', '<Layout title={`${t(\'services.ppc.hero.title\')} | Scale Automata`}>')
with open(ppc_path, 'w') as f:
    f.write(ppc_content)


# Fix data-analytics.astro title
data_path = 'src/pages/[lang]/services/data-analytics.astro'
with open(data_path, 'r') as f:
    data_content = f.read()
data_content = data_content.replace('<Layout title="Google & Social Ads | Scale Automata">', '<Layout title={`${t(\'services.data.hero.title\')} | Scale Automata`}>')
with open(data_path, 'w') as f:
    f.write(data_content)


# Fix email-marketing.astro title
email_path = 'src/pages/[lang]/services/email-marketing.astro'
with open(email_path, 'r') as f:
    email_content = f.read()
email_content = email_content.replace('<Layout title="Google & Social Ads | Scale Automata">', '<Layout title={`${t(\'services.email.hero.title\')} | Scale Automata`}>')
with open(email_path, 'w') as f:
    f.write(email_content)

# Fix social-media-marketing.astro title
social_path = 'src/pages/[lang]/services/social-media-marketing.astro'
with open(social_path, 'r') as f:
    social_content = f.read()
social_content = social_content.replace('<Layout title="Google & Social Ads | Scale Automata">', '<Layout title={`${t(\'services.social.hero.title\')} | Scale Automata`}>')
with open(social_path, 'w') as f:
    f.write(social_content)

# Fix web-and-mobile-development.astro title
web_path = 'src/pages/[lang]/services/web-and-mobile-development.astro'
with open(web_path, 'r') as f:
    web_content = f.read()
web_content = web_content.replace('<Layout title="Technical & Content SEO & GEO | Scale Automata">', '<Layout title={`${t(\'services.web.hero.title\')} | Scale Automata`}>')
with open(web_path, 'w') as f:
    f.write(web_content)


# Fix seo-geo.astro title
seo_path = 'src/pages/[lang]/services/seo-geo.astro'
with open(seo_path, 'r') as f:
    seo_content = f.read()
seo_content = seo_content.replace('<Layout title="Technical & Content SEO & GEO | Scale Automata">', '<Layout title={`${t(\'services.seo.hero.title\')} | Scale Automata`}>')
with open(seo_path, 'w') as f:
    f.write(seo_content)


# Fix services/index.astro for PPC desc that got wrongfully replaced due to duplication
services_index_path = 'src/pages/[lang]/services/index.astro'
with open(services_index_path, 'r') as f:
    services_content = f.read()

# Originally it was `<p>{t('services.index.seo.desc')}</p>` for both because the string was duplicate.
# I need to find the specific one under PPC and replace it with `{t('services.index.ppc.desc')}`
services_content = services_content.replace('<h3>{t(\'services.index.ppc.title\')}</h3>\n                <p>{t(\'services.index.seo.desc\')}</p>', '<h3>{t(\'services.index.ppc.title\')}</h3>\n                <p>{t(\'services.index.ppc.desc\')}</p>')

with open(services_index_path, 'w') as f:
    f.write(services_content)
