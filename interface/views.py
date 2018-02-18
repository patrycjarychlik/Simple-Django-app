from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from interface.forms import AddItemForm
from website.models import List, Item


# Create your views here.

@login_required
def home(request):
    if request.method == "POST":
        if 'addItem' in request.POST:
            form = AddItemForm(data=request.POST)
            if form.is_valid():
                form.save()
            form = AddItemForm()
    else:
        form = AddItemForm()
    return  render(request, "interface/home.html",
                   {
                       'items': List.objects.all(),
                       'addItemForm' : form
                    });

