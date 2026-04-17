import codecs
import re

filepath = 'src/pages/[lang]/index.astro'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

# Let's fix the missed replacements because there were some tiny differences in the text
content = re.sub(r'We craft bespoke strategies designed to elevate brand and drive measurable results\. From innovative web design to comprehensive digital campaigns, we are dedicated to achieving goals\.', "{t('index.hero.subtitle')}", content)
content = re.sub(r'<p>Unlock business potential with our advanced digital marketing and web development services\. We build custom website development solutions and budget-efficient marketing campaigns designed to generate real revenue, not just vanity metrics\. To consistently rank higher and dominate online search, marketing strategy needs than basic SEO\.</p>', "<p>{t('index.hero.desc1')}</p>", content)
content = re.sub(r'<p>\s*We utilize advanced Generative Engine Optimization \(GEO\), targeted social media ads, and data-driven web design to maximize brand visibility and website traffic\. Every landing page, email marketing campaign, and SEO optimization tactic we deploy is engineered for maximum conversion rate optimization \(CRO\) and direct online growth\.</p>', "<p>{t('index.hero.desc2')}</p>", content)
content = re.sub(r'<p>Whether it\'s driving local SEO foot traffic or boosting ecommerce sales, our transparent performance tracking ensures you know exactly where investment goes\. We don\'t hide behind industry buzzwords; we deliver practical, results-oriented web development and search engine marketing that scales efficiently\.</p>', "<p>{t('index.hero.desc3')}</p>", content)
content = re.sub(r'<p>Ready to stop losing customers to competitors\? Take Assessment to get a clear, no-nonsense roadmap for success, or Explore Services to find the exact digital solutions you need to dominate market\.</p>', "<p>{t('index.hero.desc4')}</p>", content)

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(content)
