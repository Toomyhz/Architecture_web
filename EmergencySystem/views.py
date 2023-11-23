from django.shortcuts import render

def index(request):
    return render(request, "pages/index.html")

def entrar(request):
    return render(request, "pages/login.html")

def registrar(request):
    return render(request, "pages/register.html")