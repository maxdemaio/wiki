from django.shortcuts import render
from django.http import HttpResponse
from . import util


def index(request):
    """ Homepage """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    """ Display an entry's page, or an error if not found """
    # TODO
    # Convert markdown to HTML
    # Put contents inside entry template
    if util.get_entry(entry):
        return render(request, "encyclopedia/entry.html", {
            "entry": entry
        })
    else:
        return render(request, "encyclopedia/error.html")
