from django.http import HttpResponse
from django.shortcuts import render, redirect


def welcome(request):
    return  HttpResponse("Hello Buch!");
    # if request.user.is_authenticated:
    #     return redirect('player_home')
    # else:
    #     return render(request, 'tictactoe/welcome.html')
