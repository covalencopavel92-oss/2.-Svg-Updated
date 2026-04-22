import re

with open("src/components/TopNav.astro", "r") as f:
    content = f.read()

print("servicesSubmenu check in TopNav:")
if "submenu: servicesSubmenu" in content:
    print("Found servicesSubmenu")
else:
    print("Not found servicesSubmenu")

print("\nblogSubmenu check in TopNav:")
if "submenu: blogSubmenu" in content:
    print("Found blogSubmenu")
else:
    print("Not found blogSubmenu")
