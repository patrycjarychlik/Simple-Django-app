from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ui.forms import AddItemForm, AddListForm, EditItemForm, UserCreationForm
from website.models import List, Item
from django import forms


# Create your views here.

@login_required
def home(request):
    return open_list(request, 1)

@login_required
def open_list(request, list_id):
    form = AddItemForm()
    listForm = AddListForm()
    editItemForm = EditItemForm()

    return  render(request, "ui/app.html",
                   {
                       'items': Item.objects.filter(list_id=list_id),
                       'count': Item.objects.filter(list_id=list_id).count(),
                       'lists': List.objects.filter(Q(user=request.user) | Q(id=1)),
                       'addItemForm' : form,
                       'addListForm': listForm,
                       'editItemForm': editItemForm,
                       'list_id': list_id,
                       'list_sum': Item.objects.filter(list_id=list_id).annotate(total=Sum('price')).first(),
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


@login_required
def add_list(request, list_id):
    if request.method == "POST":
        if 'addList' in request.POST:
            list = List(
                user=request.user
            )
            form = AddListForm(instance=list, data=request.POST)
            if form.is_valid():
                form.save()
            form = AddListForm()
    return open_list(request, list_id)

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "app/signup_form.html"
    success_url = reverse_lazy('list_page', kwargs={'list_id': 1},
                            current_app='myapp')


