from collections import OrderedDict
import re
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import Context, Template
import os
from cs361project1.settings import BASE_DIR


def getwords(html):
    # Remove all the HTML tags
    words = []
    for h in html:
        # Split words by all non-alpha characters
        words += re.compile(r'[^A-Z^a-z]+').split(h)
    # Convert to lowercase
    return [word.lower() for word in words if word != '']


def getwordcounts(template):
    wc = {}
    words = getwords(template)
    for word in words:
        wc.setdefault(word, 0)
        wc[word] += 1
    return wc


def wordcounter(request, filename):
    file = open(os.path.join(BASE_DIR, 'templates') + "/" + filename + ".html")
    wc = getwordcounts(file.readlines())
    t = Template("Name: {{ filename }}<br>  Words: <br>{% for x,y in wc.items %} {{ x }},{{ y }}<br> {% endfor %}")
    c = Context({'wc': wc, 'filename': filename})
    html = t.render(c)
    file.close()
    return HttpResponse(html)
