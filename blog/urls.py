#from django.contrib import admin
from django.urls import path
from django.urls import path,include
from blog.views import *

app_name = "blog"

urlpatterns = [
    path("",blog_home_view, name="blog_home"),
    path("single",blog_single_view, name="blog_single"),
]

