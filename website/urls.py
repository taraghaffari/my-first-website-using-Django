#from django.contrib import admin
from django.urls import path
from django.urls import path,include
from website.views import *

app_name = "website"

urlpatterns = [
    path("", index_view, name="index"),
    path("about", about_view,name="about"),
    path("contact/wedhgdf",contact_view,name="contact"),
    path("elements",elements_view,name="elements"),
    path("test",test_view,name="test"),
]

