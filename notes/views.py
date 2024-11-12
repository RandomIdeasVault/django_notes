#from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import App, Module, Link, Guide


class HomePageView(TemplateView):
    template_name = 'index.html'


class AppView(ListView):
    model = App
    template_name = 'apps.html'


class ModuleView(ListView):
    model = Module
    template_name = 'modules.html'


class GuideView(ListView):
    model = Guide
    template_name = 'guides.html'


class LinkView(ListView):
    model = Link
    template_name = 'links.html'
