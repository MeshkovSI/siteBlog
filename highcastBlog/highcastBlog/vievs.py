from django.http import  HttpResponse
from django.shortcuts import render

MENU = {"HIGHCAST":"/", "Main":"/", "About":"/about"}

def main_page(request):
    title = "Main Page"
    data = {"menu": MENU, "title": title}
    return render(request, "./index.html", context=data)

def post_page(request):
    title = "Post"
    data = {"menu": MENU, "title": title}
    return render(request, "./post.html", context=data)

def about_page(request):
    title = "About"
    data = {"menu": MENU, "title": title}
    return render(request, "./about.html", context=data)

