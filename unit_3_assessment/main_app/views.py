from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from .models import Widget
from .forms import WidgetsForm
from django.db.models import Sum

# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    total = Widget.objects.all().aggregate(Sum('quantity'))['quantity__sum']
    widgets_form = WidgetsForm()
    return render(request, 'index.html', {
        'total': total,
        'widgets': widgets,
        'form': widgets_form
    })

def add_widget(request):
    form = WidgetsForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('index')

def delete_widget(request, id):
    Widget.objects.get(id=id).delete()
    return redirect('index')

