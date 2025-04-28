#simple function fo slugify(title)
import re

def slugify(title):
    title = title.lower()

    title = re.sub(r'[\s_]+', '-', title)

    title = re.sub(r'[^a-z0-9-]', '', title)

    title = title.strip('-')
    return title