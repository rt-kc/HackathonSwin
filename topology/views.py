from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
# from .form import MyForm
from .models import SwitchConfig
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView,DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CreateConfigCLI(CreateView):
    model = SwitchConfig
    fields = ['input_data', 'output']
    success_url = 'config'
    template_name = 'addconfig.html'

class ViewListConfig(ListView):
    model = SwitchConfig
    context_object_name = "configs"
    template_name = "viewlistconfig.html"

class DeleteConfig(DeleteView):
    model = SwitchConfig
    template_name = "deleteconfig.html"
    success_url = "/topology/config"
class ConfigDetail(DetailView):
    model = SwitchConfig
    context_object_name = "config"
    template_name = "configdetail.html"
    # login_url = "/login"
class RunScript():
    
    


