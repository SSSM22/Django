from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"go/index.html")
def hello(request):
    return HttpResponse("Hello Sai SHiva Mani")
def Shiva(request):
    return HttpResponse("hey SHiva")

def contact(request):
    return render(request,"go/contact.html")
def login(request):
    return render(request,"go/login.html")
def welcome(request):
    return render(request,"go/welcome.html",)