from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from . import util

class NewEditForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    contents = forms.CharField(label="Contents", widget=forms.Textarea)

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
        # TODO Make changes for the edits made

        # Create a form instance and populate it with data from the request
        form = NewEditForm(request.POST)

        # Check whether form is valid
        if form.is_valid():
            # TODO Process the data and redirect
            title = form.cleaned_data['title']
            contents = form.cleaned_data['contents']
            return redirect(reverse('viewEntry', kwargs={'entry': entry}))
        else:
            title = util.get_title(entry)
            contents = util.read_contents(entry)
            form = NewEditForm({"title": title, "contents": contents})
            return render(request, "encyclopedia/edit.html", {
                "form": form,
                "entry": entry,
                "contents": contents,
                "title": title
            })
    else:
        if util.get_entry(entry):
            title = util.get_title(entry)
            contents = util.read_contents(entry)
            form = NewEditForm({"title": title, "contents": contents})
            return render(request, "encyclopedia/edit.html", {
                "form": form,
                "entry": entry,
                "contents": contents,
                "title": title
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "error": "404 Error, this page does not exist"
            })
            