from django.shortcuts import render
from django.views.generic.edit import DeleteView
from .models import Widgets
from .forms import WidgetsForm

# Create your views here.
def index(request):
    form = WidgetsForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
    return render(request, 'index.html', {
        'form': form,
        
    })
