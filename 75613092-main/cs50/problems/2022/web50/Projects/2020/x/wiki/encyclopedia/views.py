from django.shortcuts import render
import markdown2
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_entries(request, title):
    get_md = util.get_entry(title)
    if get_md is None:
        return render(request, "encyclopedia/error.html", {"error" : "404 - Page does not exist"})
    html_content = markdown2.markdown(get_md)
    return render(request, "encyclopedia/entry_page.html", {
        "title": title,
        "content": html_content
    })

def fetch(request, searched=None):
    if request.method=='POST':
        entries= request.POST['q']
        html_content = util.get_entry(entries)
        if html_content is not None:
            html_content = markdown2.markdown(html_content)
            return render(request, "encyclopedia/entry_page.html", {
                "title":entries,
                "content":html_content
            })
        else:
            all_entries = util.list_entries()
            found = []
            count = 0
            for match in all_entries:
                if entries.lower() in match.lower():
                    count += 1
                    found.append(match)
            if count == 0:
                return render(request, "encyclopedia/error.html", {
                    "error":"Page not found"
                })
            return render(request, "encyclopedia/fetch.html", {
                "reco": found,
            })
    elif searched:  # Handle GET request with searched parameter
        html_content = util.get_entry(searched)
        if html_content is not None:
            html_content = markdown2.markdown(html_content)
            return render(request, "encyclopedia/entry_page.html", {
                "title": searched,
                "content": html_content
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "error": "Page not found"
            })
    else:  # Handle GET request without searched parameter (initial load)
        return render(request, "encyclopedia/fetch.html", {
            "reco": []
        })




def new_page(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/new_page.html")
    else:
        title = request.POST['page_title']
        content = request.POST['content']
        isTitle = util.get_entry(title)
        if isTitle is not None:
            return render(request, "encyclopedia/error.html", {
                "error":"Page already exist"
            })
        util.save_entry(title, content)
        title = util.get_entry(title)
        html_content = markdown2.markdown(title)
        return render(request, "encyclopedia/entry_page.html",
                      {
                          "title":title,
                          "content":html_content
                      })


def edit(request):
    if request.method == 'POST':
        title = request.POST['edit']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title":title,
            "content":content
        })
def save(request):
    if request.method == 'POST':
        title = request.POST['page_title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = util.get_entry(title)
        html_content = markdown2.markdown(html_content)
        return render(request, "encyclopedia/entry_page.html", {
            "title":title,
            "content":html_content
            })

def rand(request):
    values = util.list_entries()
    values = random.choice(values)
    values = util.get_entry(values)
    html_content = markdown2.markdown(values)
    return render(request, "encyclopedia/entry_page.html", {
        "title":values,
        "content": html_content
    })









