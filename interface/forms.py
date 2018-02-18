from django.forms import ModelForm

from website.models import Item

class AddItemForm(ModelForm):
    class Meta:
        model = Item
        exclude = ('date', 'marked')
