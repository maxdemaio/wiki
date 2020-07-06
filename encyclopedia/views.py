from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from . import util


def index(request):
    """ Homepage """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def view_entry(request, entry):
    """ Display an entry's page, or an error if not found """
    if util.get_entry(entry):
        return render(request, "encyclopedia/entry.html", {
            "entry": entry,
            "contents": util.convert_md(entry),
            "title": util.get_title(entry)
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "404 Error, this page does not exist"
        })

def edit_entry(request, entry):
    """ Allow a user to edit an entry """
    if request.method == "POST":
        return redirect(reverse('viewEntry', kwargs={'entry': entry}))
    else:
        if util.get_entry(entry):
            return render(request, "encyclopedia/edit.html", {
                "entry": entry,
                "contents": util.read_contents(entry),
                "title": util.get_title(entry)
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "error": "404 Error, this page does not exist"
            })
