from django.http import HttpResponse
from django.shortcuts import render, redirect


def welcome(request):
    return  HttpResponse("Hello Buch!");

