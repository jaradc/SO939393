from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import ModelTwoForm
from .models import ModelTwo

class HomeView(ListView):
    model = ModelTwo
    template_name = 'myapp/base.html'

class Create(CreateView):
    form_class = ModelTwoForm
    model = ModelTwo
    template_name = 'myapp/create_form.html'
    success_url = '/'



