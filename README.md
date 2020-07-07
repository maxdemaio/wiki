# Wiki
#### Wikipedia-like online encyclopedia (Markdown to HTML)

## Overview
Wiki is a Django application that allows users to view, create, and edit entries in its encyclopedia. Each entry is stored server side in a lightweight Markdown file. When looking at an entry's page, the markdown is converted to HTML using the `markdown2` Python library. The raw markdown can also be viewed/edited when going into the edit mode of a specific page.

There is a random page link that will redirect the user to a random page from the list of existing encyclopedia entries. Also, one can search for entries using the search bar. If the query matches an entry, the user is redirected to that entry's page. If the query is a substring of any entry, a list will be created for navigation.

In conclusion, to add to the encyclopedia one can click the "Create New Page" link. All that's needed to create a new entry is to type in a title and the markdown contents to be stored.
