import codecs
import re

filepath = 'src/pages/[lang]/index.astro'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

content = content.replace("{t(\\'index.hero.title\\')}", "{t('index.hero.title')}")

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(content)
