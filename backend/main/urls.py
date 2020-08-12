"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os

from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from backend.app01.views import render_app01_index

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^$", render_app01_index),
    # Stylesheets
    url(
        r"^css/(?P<path>.*)$",
        serve,
        {
            "document_root": os.path.join(
                settings.BASEDIR, "frontend", "dist", "css"
            ),
        },
    ),
    # Scripts
    url(
        r"^js/(?P<path>.*)$",
        serve,
        {
            "document_root": os.path.join(
                settings.BASEDIR, "frontend", "dist", "js"
            ),
        },
    ),
]
