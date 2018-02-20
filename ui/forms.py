from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, forms

from website.models import Item, List, Category, Service, Budget


class AddItemForm(ModelForm):
    class Meta:
        model = Item
        exclude = ('date', 'marked', 'list')

class EditItemForm(ModelForm):
    class Meta:
        model = Item
        exclude = ('date', 'marked', 'list')

class AddListForm(ModelForm):
    class Meta:
        model = List
        exclude = ('date', 'user')


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = ""


class AddServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ('date', 'category')


class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ('date', 'user')

class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        exclude = ('user',)
