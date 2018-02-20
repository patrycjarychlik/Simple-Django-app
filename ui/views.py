from distutils.command import register

from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum, Count, Subquery, OuterRef
from django.forms import forms
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ui.forms import AddItemForm, AddListForm, EditItemForm, UserCreationForm, AddCategoryForm, \
    AddServiceForm, BudgetForm
from website.models import List, Item, Category, Service, Budget
from django.db import models

class SQCount(Subquery):
    template = "(SELECT count(*) FROM (%(subquery)s) _count)"
    output_field = models.IntegerField()


@login_required
def home(request):
    return open_list(request, 0)

@login_required
def open_list(request, list_id):
    form = AddItemForm()
    listForm = AddListForm()
    editItemForm = EditItemForm()
    items = Item.objects.filter(list_id=list_id, marked=False)
    itemsDone = Item.objects.filter(list_id=list_id, marked=True)

    if list_id == 0:
        items = Item.objects.filter(list__user=request.user, marked=False)
        itemsDone = Item.objects.filter(list__user=request.user, marked=True)

    active=Item.objects.filter(marked=False, list_id=OuterRef('pk')).values('pk')
    lists=List.objects.filter(user=request.user).annotate(number_of=SQCount(active))

    return  render(request, "ui/app.html",
                   {
                       'active_tab' : 'todo_list',
                       'items': items,
                       'items_done': itemsDone,
                       'count': Item.objects.filter(list_id=list_id).count,
                       'lists': lists,
                       'addItemForm' : form,
                       'addListForm': listForm,
                       'editItemForm': editItemForm,
                       'list_id': list_id,
                       'list': List.objects.filter(id=list_id).first()
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
def mark_done(request, item_id, list_id):
    if request.method == "POST":
        item = Item.objects.get(pk=item_id)
        if item.marked == True:
            item.marked=False
        else:
            item.marked=True
        item.save()
    return open_list(request, list_id)\

@login_required
def delete_list(request, list_id):
    if request.method == "POST":
        list = get_object_or_404(List, pk=list_id)
        list.delete()
    return open_list(request, 0)


@login_required
def add_list(request, list_id):
    if request.method == "POST":
        if 'addList' in request.POST:
            list = List(
                user=request.user
            )
            form = AddListForm(instance=list, data=request.POST)
            if form.is_valid():
                updated=form.save()
                return open_list(request,  updated.id)
    form = AddListForm()
    return open_list(request, list_id)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "app/signup_form.html"
    success_url = reverse_lazy('list_page', kwargs={'list_id': 1},
                            current_app='myapp')


@login_required
def money(request):
    return open_money(request, 0)

@login_required
def open_money(request, list_id):
    form = AddServiceForm(initial={'price': '0.00'})
    listForm = AddCategoryForm()
    budget_init=Budget.objects.get_or_create(user=request.user)[0];
    budgetForm = BudgetForm(instance=budget_init)

    items =  Service.objects.filter(category_id=list_id);
    sum=Service.objects.filter(category_id=list_id).aggregate(Sum('price'))['price__sum']
    sum_all = Service.objects.filter(category__user=request.user).aggregate(Sum('price'))['price__sum']

    if list_id == 0:
        items= Service.objects.filter(category__user=request.user);
        sum=sum_all;

    budget=Budget.objects.filter(user=request.user).first()

    calculations=(1-(sum_all or 0)/(budget.value or 1))*100
    if calculations:
        percent=calculations
    else:
        percent=0

    return  render(request, "ui/money.html",
                   {
                       'active_tab': 'money',
                       'items':items,
                       'budget': budget,
                       'count': Service.objects.filter(category_id=list_id).count(),
                       'lists': Category.objects.filter(Q(user=request.user)),
                       'addItemForm' : form,
                       'addListForm': listForm,
                       'addBudgetForm': budgetForm,
                       'list_id': list_id,
                       'list': Category.objects.filter(id=list_id).first(),
                       'list_sum': sum,
                       'percent':percent

                   })

@login_required
def add_service(request, list_id):
    if request.method == "POST":
        if 'addItem' in request.POST:
            item = Service(
                category_id=list_id
            )
            form = AddServiceForm(instance=item, data=request.POST)
            if form.is_valid():
                form.save()
            form = AddServiceForm()
    return open_money(request, list_id)


@login_required
def delete_service(request, item_id, list_id):
    if request.method == "POST":
        item = get_object_or_404(Service, pk=item_id)
        item.delete()
    return open_money(request, list_id)

@login_required
def delete_category(request, list_id):
    if request.method == "POST":
        category = get_object_or_404(Category, pk=list_id)
        category.delete()
    return open_money(request, 0)

@login_required
def add_category(request, list_id):
    if request.method == "POST":
        if 'addList' in request.POST:
            list = Category(
                user=request.user
            )
            form = AddCategoryForm(instance=list, data=request.POST)
            if form.is_valid():
                updated=form.save()
                return open_money(request, updated.id)
    form = AddCategoryForm()
    return open_money(request, list_id)

@login_required
def edit_budget(request,list_id):
    if request.method == "POST":
        form = BudgetForm(data=request.POST)
        budget = Budget.objects.get_or_create(user=request.user)[0]
        budget.value=form.data['value'];
        budget.save()
    return open_money(request, list_id)

