import codecs
import re

# Fix index.astro wave animation
index_path = 'src/pages/[lang]/index.astro'
with codecs.open(index_path, 'r', 'utf-8') as f:
    index_content = f.read()

# I need to restore the wave-word functionality. The original was:
# <span class="wave-word" style="--d:0.2s">Enhance </span>
# <span class="wave-word" style="--d:0.4s">your </span>
# <span class="wave-word" style="--d:0.6s">strategy.</span><br/>
# <span class="wave-word" style="--d:0.8s">Rank </span>
# <span class="wave-word" style="--d:1s">higher. </span>
# <span class="wave-word" style="--d:1.2s">Get </span>
# <span class="wave-word" style="--d:1.4s">more </span>
# <span class="wave-word" style="--d:1.6s">customers.</span>

# I'll modify index.astro to dynamically map words to spans, but since translations change the number of words, it's better to just do it via JS or keep the full sentence in one span. However, the feedback said "replacing the multiple <span class="wave-word"> tags with a single tag containing the entire title breaks the staggered word-by-word wave animation effect intended by the original markup".

# A good way is to split the translated string in Astro and render the spans.
wave_replacement = """
                        {t('index.hero.title').split(' ').map((word, index) => (
                            <>
                            <span class="wave-word" style={`--d:${0.2 + index * 0.2}s`}>{word} </span>
                            {word.endsWith('.') && <br/>}
                            </>
                        ))}
"""

# Let's replace the single span we injected with this
index_content = re.sub(r'<span class="wave-word" style="--d:0\.2s">\{t\(\'index\.hero\.title\'\)\}</span>', wave_replacement, index_content)

with codecs.open(index_path, 'w', 'utf-8') as f:
    f.write(index_content)
