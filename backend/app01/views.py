import os

from django.shortcuts import render


def render_app01_index(request):
    return render(request, os.path.join("app01", "index.html"))
