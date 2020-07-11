from django.forms import ModelForm
from .models import Widgets

class WidgetsForm(ModelForm):
    class Meta:
        model = Widgets
        fields = ['description', 'quantity']