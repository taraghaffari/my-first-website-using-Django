from django.shortcuts import render

def blog_home_view(request):
    return render(request, "blog/blog-home.html")

def blog_single_view(request):
    context = {"title": "My Blog", "content": "Hello I'm Tara and this is my blog"}
    return render(request, "blog/blog-single.html",context)

