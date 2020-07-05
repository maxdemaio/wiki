from django.shortcuts import render
from django.http import HttpResponse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    if util.get_entry(entry):
        return HttpResponse(f"This is entry {entry}")
    else:
        return HttpResponse("This is an error, no entry found")