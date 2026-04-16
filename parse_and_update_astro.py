import os
import re

updates = {
    'src/pages/[lang]/index.astro': [
        ('Enhance ', "{t('index.hero.title').split('.')[0] + '. '}"),
        ('your ', ""),
        ('strategy.', ""),
        ('Rank ', "{t('index.hero.title').split('.')[1] + '. '}"),
        ('higher. ', ""),
        ('Get ', "{t('index.hero.title').split('.')[2] + '.'}"),
        ('more ', ""),
        ('customers.', ""),
        ('We craft bespoke strategies designed to elevate your brand and drive measurable results. From innovative web design to comprehensive digital campaigns, we are dedicated to achieving your goals.', "{t('index.hero.subtitle')}"),
        ('Unlock your business potential with our advanced digital marketing and web development services. We build custom website development solutions and budget-efficient marketing campaigns designed to generate real revenue, not just vanity metrics. To consistently rank higher and dominate online search, your marketing strategy needs more than basic SEO.', "{t('index.hero.desc1')}"),
        ('We utilize advanced Generative Engine Optimization (GEO), targeted social media ads, and data-driven web design to maximize your brand visibility and website traffic. Every landing page, email marketing campaign, and SEO optimization tactic we deploy is engineered for maximum conversion rate optimization (CRO) and direct online growth.', "{t('index.hero.desc2')}"),
        ("Whether it's driving local SEO foot traffic or boosting ecommerce sales, our transparent performance tracking ensures you know exactly where your investment goes. We don't hide behind industry buzzwords; we deliver practical, results-oriented web development and search engine marketing that scales efficiently.", "{t('index.hero.desc3')}"),
        ("Ready to stop losing customers to your competitors? Take Assessment to get a clear, no-nonsense roadmap for your success, or Explore Services to find the exact digital solutions you need to dominate your market.", "{t('index.hero.desc4')}")
    ],
    'src/pages/[lang]/services/index.astro': [
        ('SEO &amp; GEO', "{t('services.index.seo.title')}"),
        ('SEO & GEO', "{t('services.index.seo.title')}"),
        ('Dominate search results and drive organic traffic.', "{t('services.index.seo.desc')}"),
        ('PPC &amp; Social Ads', "{t('services.index.ppc.title')}"),
        ('PPC & Social Ads', "{t('services.index.ppc.title')}"),
        ('Acquire high-intent leads and maximize your return on ad spend.', "{t('services.index.ppc.desc')}"),
        ('Dominate search results and drive organic traffic.', "{t('services.index.seo.desc')}"), # Wait, ppc desc was duplicate in file, I will fix it by regex instead
    ],
    'src/pages/[lang]/services/seo-geo.astro': [
        ('Technical &amp; Content<br/>SEO &amp; GEO', "{t('services.seo.hero.title')}"),
        ('Technical & Content<br/>SEO & GEO', "{t('services.seo.hero.title')}"),
        ('We execute deep technical audits, build high-authority backlinks, and craft optimized content that ranks.', "{t('services.seo.hero.subtitle')}"),
        ('Right now, potential customers are searching for exactly what you offer. The question is: Are they finding you, or your competitors? We know you need rapid growth and a clear path to increase sales without paying an exorbitant price. Our unified approach to SEO and Geo ensures your brand is visible exactly where it matters most.', "{t('services.seo.hero.desc1')}"),
        ("People don't scroll past the first page; they trust the top results. We get you there. By combining deep technical website audits with high-authority backlinking, we force the search engine to recognize your authority.", "{t('services.seo.hero.desc2')}"),
        ("Whether a user is typing a query into Google Search or asking a generative AI on Bing Search, we ensure your business climbs the ranking. We don't just aim for traffic; we aim for the right page results that bring buyers directly to your site. Practical, transparent, and built for conversion.", "{t('services.seo.hero.desc3')}"),
        ('Start Growing', "{t('services.seo.hero.button')}")
    ],
    'src/pages/[lang]/services/data-analytics.astro': [
        ('Business Intelligence &amp; Data Analytics', "{t('services.data.hero.title')}"),
        ('Business Intelligence & Data Analytics', "{t('services.data.hero.title')}"),
        ('Implementation of GA4, Tag Manager, and Looker Studio for real-time visibility into your KPIs.', "{t('services.data.hero.subtitle')}"),
        ('Why Data Analytics Matters?', "{t('services.data.hero.desc1')}"),
        ('Behind every number is a real person interacting with your brand, and understanding data is simply learning how to serve them better. We use compassionate data analysis to help you listen to your community. By tracking your key performance indicators, we discover exactly what your audience values most. We implement secure G4A and Google Analytics to monitor performance metrics across all your touchpoints—from social media interactions and Google Ads to the engagement of your email list.', "{t('services.data.hero.desc2')}"),
        ("Your community's trust is paramount, which is why we guarantee complete GDPR alignment and flawless data safety. Rather than obsessing over the competition, we use market research and thoughtful competition research to find unique ways your business can shine. We rely on authentic data storytelling to translate complex metrics and trends into actionable advice. By keeping a close eye on every vital KPI, we empower you to create performance-driven marketing campaign strategies that resonate deeply with your customers and foster sustainable, long-term success.", "{t('services.data.hero.desc3')}"),
        ('Check new ways to grow your business with data analytics!', "{t('services.data.hero.button')}")
    ],
    'src/pages/[lang]/services/email-marketing.astro': [
        ('KEEP YOUR CUSTOMERS COMING BACK WITH EMAIL MARKETING', "{t('services.email.hero.title')}"),
        ('Advanced segmentation, drip campaigns, and engaging newsletters that turn subscribers into buyers and keep your audience connected to your brand.', "{t('services.email.hero.subtitle')}"),
        ('Sustainable growth comes from treating your audience with genuine respect and delivering consistent value. A thoughtfully managed email marketing campaign is an indispensable asset for nurturing those vital relationships safely. We empower you to deeply know your customers and serve them better through highly personalized email marketing. By implementing intelligent email automation, we ensure you reliably reach the right audience at the right time.', "{t('services.email.hero.desc1')}"),
        ('Our team crafts compelling email marketing content, from informative, engaging newsletters that share your expertise, to tasteful promotional emails designed to naturally increase conversions. We also focus heavily on the post-purchase journey, utilizing targeted retention email strategies to solidify long-term customer loyalty. To keep your brand fresh, we carefully leverage the latest trends to create visually appealing and engaging content.', "{t('services.email.hero.desc2')}"),
        ("Most importantly, we protect the trust you have built with your community by guaranteeing total data safety, strict GDPR standards, and absolute compliance in every send. Partner with us to comfortably reach your goals while respecting your subscribers.", "{t('services.email.hero.desc3')}"),
        ('Personalyze Your Email Marketing Strategy Today!', "{t('services.email.hero.button')}")
    ],
    'src/pages/[lang]/services/ppc-and-social-ads.astro': [
        ('Google &amp; Social Ads', "{t('services.ppc.hero.title')}"),
        ('Google & Social Ads', "{t('services.ppc.hero.title')}"),
        ('Data-backed campaign management across Google Ads, Meta, LinkedIn, and TikTok to acquire high-intent leads and maximize your return on ad spend.', "{t('services.ppc.hero.subtitle')}"),
        ('Your business offers real value, and there are countless people out there looking for exactly what you provide. The true power of digital marketing is simply bridging that gap. We understand that navigating paid advertisement online can feel overwhelming, especially with a careful budget. That is where we step in as your respectful partner.', "{t('services.ppc.hero.desc1')}"),
        ('Utilizing PPC (Pay per Click) is an indispensable tool to reach the right audience at the exact moment they need you. We focus on a pay-per-customer model that honors your investment, maximizing your Return on ad spend (ROAS). To truly elevate your online presence and increase sales, we strategically utilize social media. We connect you with your community through authentic Facebook ads and inspiring Instagram Ads. We also help you share your story through impactful video ads on platforms like TikTok and X.', "{t('services.ppc.hero.desc2')}"),
        ("This isn't just about gaining more followers; it's about building meaningful relationships that sustain your business. By managing your campaigns with deep care, we ensure every euro helps you grow confidently.", "{t('services.ppc.hero.desc3')}"),
        ('Ready to Grow?', "{t('services.ppc.hero.button')}")
    ],
    'src/pages/[lang]/services/social-media-marketing.astro': [
        ('Organic &amp; Viral Growth', "{t('services.social.hero.title')}"),
        ('Organic & Viral Growth', "{t('services.social.hero.title')}"),
        ('Content calendars, community management, and trend-jacking strategies to amplify your brand voice and foster authentic connections with your audience across all major social platforms.', "{t('services.social.hero.subtitle')}"),
        ('Building a loyal community takes time, but it is one of the most rewarding ways to expand business. We offer supportive digital marketing services designed to lift that burden and help you expand your business smoothly. If you want to get known on social media without the high cost of constant ads or paid media, a strong organic social media strategy is the most effective path. Our marketing services handle your complete profile administration, ensuring your voice is consistent and professional.', "{t('services.social.hero.desc1')}"),
        ('We actively monitor current trends among potential customers through social listening on diverse media channels so you can meaningfully communicate with your audience. Whether we are designing visually creative posts for Instagram and Facebook, producing dynamic videos for TikTok, sparking professional dialogue on LinkedIn, or engaging directly on X, we create truly engaging content.', "{t('services.social.hero.desc2')}"),
        ("While online advertising has its place to quickly reach customers, building trust organically is highly cost-effective. By managing your social media marketing with care, we give you the freedom to focus on your core business while your online community flourishes naturally. Growing your community shouldn't require an exorbitant cost, but rather a thoughtful, dedicated strategy that honors your business goals.", "{t('services.social.hero.desc3')}"),
        ('Reach your Audience', "{t('services.social.hero.button')}")
    ],
    'src/pages/[lang]/services/web-and-mobile-development.astro': [
        ('Modern Web &amp; Mobile Development', "{t('services.web.hero.title')}"),
        ('Modern Web & Mobile Development', "{t('services.web.hero.title')}"),
        ('Build high-performance, conversion-optimized websites and mobile applications.', "{t('services.web.hero.subtitle')}"),
        ('Every business has a unique story, and sharing it clearly with your customers is essential. A thoughtfully crafted website acts as your most welcoming digital storefront. Investing in quality web development is indispensable because it creates a comfortable space where people can easily connect with the value you provide.', "{t('services.web.hero.desc1')}"),
        ('When your audience clicks through from thoughtful ads or search results, they expect a smooth, fast loading journey. Partnering with an empathetic developer ensures your vision comes to life exactly as you imagine. Through careful website optimization and robust security, we protect your audience while helping you organically increase traffic and secure a valuable spot on the first page. A clean, modern looking digital presence builds immediate trust.', "{t('services.web.hero.desc2')}"),
        ("Whether your brand calls for a minimalist, simple design to highlight your core message, or engaging, complicated designs, animations, and immersive layouts to captivate attention, we build exactly what you need. Every site is deeply interactive and entirely responsive, guaranteeing that every visitor feels valued.", "{t('services.web.hero.desc3')}"),
        ('Build Your Story', "{t('services.web.hero.button')}")
    ],
}

import codecs

for filepath, replacements in updates.items():
    if not os.path.exists(filepath):
        continue
    with codecs.open(filepath, 'r', 'utf-8') as f:
        content = f.read()

    if filepath == 'src/pages/[lang]/index.astro':
        # Custom logic for index.astro wave-words because we can't just replace them blindly due to formatting.
        content = re.sub(r'<span class="wave-word"[^>]*>Enhance </span>\s*<span class="wave-word"[^>]*>your </span>\s*<span class="wave-word"[^>]*>strategy\.</span><br/>\s*<span class="wave-word"[^>]*>Rank </span>\s*<span class="wave-word"[^>]*>higher\. </span>\s*<span class="wave-word"[^>]*>Get </span>\s*<span class="wave-word"[^>]*>more </span>\s*<span class="wave-word"[^>]*>customers\.</span>',
                         r'<span class="wave-word" style="--d:0.2s">{t(\'index.hero.title\')}</span>', content)

    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
        else:
            # Maybe strip spaces and retry
            # We don't want to get stuck.
            pass

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content)


# Custom logic for services/index.astro
services_index_path = 'src/pages/[lang]/services/index.astro'
with open(services_index_path, 'r') as f:
    services_content = f.read()

services_content = services_content.replace('<h3>SEO & GEO</h3>', "<h3>{t('services.index.seo.title')}</h3>")
services_content = services_content.replace('<p>Dominate search results and drive organic traffic.</p>', "<p>{t('services.index.seo.desc')}</p>", 1)

services_content = services_content.replace('<h3>PPC & Social Ads</h3>', "<h3>{t('services.index.ppc.title')}</h3>")
services_content = services_content.replace('<p>Dominate search results and drive organic traffic.</p>', "<p>{t('services.index.ppc.desc')}</p>")

services_content = services_content.replace('<h3>Web & Mobile Development</h3>', "<h3>{t('services.index.web.title')}</h3>")
services_content = services_content.replace('<p>High-performance conversion-optimized websites.</p>', "<p>{t('services.index.web.desc')}</p>")

services_content = services_content.replace('<h3>Social Media Marketing</h3>', "<h3>{t('services.index.social.title')}</h3>")
services_content = services_content.replace('<p>Bring community and brand loyalty.</p>', "<p>{t('services.index.social.desc')}</p>")

services_content = services_content.replace('<h3>Email Marketing</h3>', "<h3>{t('services.index.email.title')}</h3>")
services_content = services_content.replace('<p>Automate nurturing and boost customer retention.</p>', "<p>{t('services.index.email.desc')}</p>")

services_content = services_content.replace('<h3>Data Analytics</h3>', "<h3>{t('services.index.data.title')}</h3>")
services_content = services_content.replace('<p>Make informed decisions with custom dashboards.</p>', "<p>{t('services.index.data.desc')}</p>")

with open(services_index_path, 'w') as f:
    f.write(services_content)


# Sidebar.astro
sidebar_path = 'src/components/Sidebar.astro'
with open(sidebar_path, 'r') as f:
    sidebar_content = f.read()

sidebar_content = sidebar_content.replace('Lock/Unlock Sidebar', "{t('sidebar.lock')}")
sidebar_content = sidebar_content.replace('Search...', "{t('sidebar.search')}")
sidebar_content = sidebar_content.replace('0748198534', "{t('sidebar.phone')}")

with open(sidebar_path, 'w') as f:
    f.write(sidebar_content)
