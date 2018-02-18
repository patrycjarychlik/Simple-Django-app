from django.http import HttpResponse
from django.shortcuts import render, redirect


def welcome(request):
    if request.user.is_authenticated:
        return redirect('user_page')
    else:
        return  render(request, "app/welcome.html")

