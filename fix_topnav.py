import re

with open("src/components/TopNav.astro", "r") as f:
    content = f.read()

# The previous replace probably failed because of indentation or line endings.
# Let's use regex to replace just the submenu arrays.

# Replace services submenu
content = re.sub(
    r'label:\s*t\("nav\.services"\),\s*submenu:\s*\[.*?\](,|)',
    r'label: t("nav.services"),\n\t\tsubmenu: servicesSubmenu,',
    content,
    flags=re.DOTALL
)

# Replace blog submenu
content = re.sub(
    r'label:\s*t\("nav\.blog"\),\s*submenu:\s*\[.*?\](,|)',
    r'label: t("nav.blog"),\n\t\tsubmenu: blogSubmenu,',
    content,
    flags=re.DOTALL
)

with open("src/components/TopNav.astro", "w") as f:
    f.write(content)
