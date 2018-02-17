from django.shortcuts import render
from website.models import List

# Create your views here.


def home(request):
    return  render(request, "interface/home.html",
                   {'items': List.objects.all()});