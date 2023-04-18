from django.urls import path
from django.contrib import admin 
from go import views


urlpatterns=[
    path("",views.index,name="index"),
    path("hello",views.hello,name="hello"),#route/function which has to run /name for that response
    path("shiva",views.Shiva,name="shiva"),
    #path("<str:name>",views.fun,name="greet"),
    path("contact",views.contact,name="contact"),
    path("login",views.login,name="login"),
    path("welcome",views.welcome,name="welcome")
]