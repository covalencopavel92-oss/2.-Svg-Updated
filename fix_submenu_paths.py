import re

with open("src/components/Sidebar.astro", "r") as f:
    sidebar_content = f.read()

with open("src/components/TopNav.astro", "r") as f:
    topnav_content = f.read()


# We need to make sure `url` calculation uses the proper lang directory structure and strips '.astro' appropriately
# Currently the slug is path.split("/").pop()?.replace(".astro", "") || "";
# And url is `/${lang}/services/${slug}`;

# Let's inspect how the sidebar code renders the URLs
# It looks like:
# const url = `/${lang}/services/${slug}`;
# return { href: `${url}/`, label };

# In the HTML output:
# <a href="/[lang]/services/data-analytics/"
# Wait, why is it `/[lang]/...` instead of `/en/...`?
# Ah! `lang` inside the `.map()` loop might not be bound to the Astro.params.lang!
# Actually, the file uses `lang` from the module scope.
# But Astro statically analyzes `const lang = ...` and it might be problematic if used inside `import.meta.glob` or evaluated at module level if it's evaluated once for all pages...
# No, `lang` is evaluated per component render.
# BUT `import.meta.glob` is eager and module-level in some contexts... wait.
# Oh, the `.map` happens inside the component body, or outside?
