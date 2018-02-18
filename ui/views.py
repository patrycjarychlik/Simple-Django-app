from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from ui.forms import AddItemForm
from website.models import List, Item


# Create your views here.

@login_required
def home(request):
    return open_list(request, 1)

@login_required
def open_list(request, list_id):
    form = AddItemForm()
    return  render(request, "ui/app.html",
                   {
                       'items': Item.objects.filter(list_id=list_id),
                       'count': Item.objects.filter(list_id=list_id).count(),
                       'lists': List.objects.all(),
                       'addItemForm' : form,
                       'list_id': list_id
                    })

@login_required
def add_item(request, list_id):
    if request.method == "POST":
        if 'addItem' in request.POST:
            item = Item(
                list_id=list_id
            )
            form = AddItemForm(instance=item, data=request.POST)
            if form.is_valid():
                form.save()
            form = AddItemForm()
    return open_list(request, list_id)

@login_required
def delete_item(request, item_id, list_id):
    if request.method == "POST":
        item = get_object_or_404(Item, pk=item_id)
        item.delete()
    return open_list(request, list_id)


