from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.jinja",{"name":"Arya"})

def layout(request):
    return render(request,"layout.html",{"name":"Arya"})

def info(request):
    return render(request,"info.jinja",{"name":"Arya"})

def jinja_page(request):
    return render(request,"dashboard.jinja",{"name":"Arya"})