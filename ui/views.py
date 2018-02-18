from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from ui.forms import AddItemForm
from website.models import List, Item


# Create your views here.

@login_required
def home(request):
    if request.method == "POST":
        if 'addItem' in request.POST:
            item = Item(
                list_id=1
            )
            form = AddItemForm(instance=item, data=request.POST)
            if form.is_valid():
                form.save()
            form = AddItemForm()
    else:
        form = AddItemForm()
    return  render(request, "ui/home.html",
                   {
                       'items': Item.objects.filter(list_id=1),
                       'lists': List.objects.all(),
                       'addItemForm' : form
                    })

@login_required
def open_list(request, list_id):
    form = AddItemForm()
    return  render(request, "ui/home.html",
                   {
                       'items': Item.objects.filter(list_id=list_id),
                       'lists': List.objects.all(),
                       'addItemForm' : form
                    })


