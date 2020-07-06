import os
import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from markdown2 import Markdown


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


def convert_md(mdFile):
    """ 
    Read contents of Markdown file and return HTML. 
    """
    with open(f"./entries/{mdFile}.md") as f:
        contents = f.read()
    markdowner = Markdown()
    ourHtml = markdowner.convert(contents)
    return ourHtml


def get_title(mdFile):
    base = os.path.basename(f"./entries/{mdFile}.md")
    title = os.path.splitext(base)[0]
    return title


def read_contents(mdFile):
    """ 
    Return the contents of a Markdown file. 
    """
    with open(f"./entries/{mdFile}.md") as f:
        contents = f.read()
    return contents


# TODO Change title and contents of a file
def change_title_contents(prevTitle, newTitle, newContents):
    """
    Change the title and contents of a Markdown file.
    """
    os.rename(f"./entries/{prevTitle}.md", f"./entries/{newTitle}.md")
    with open(f"./entries/{newTitle}.md", "w") as f:
        f.write(newContents)
    return
