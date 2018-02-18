from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from website.models import List

# Create your views here.

@login_required
def home(request):
    return  render(request, "interface/home.html",
                   {'items': List.objects.all()});
