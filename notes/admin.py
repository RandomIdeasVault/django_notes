from django.contrib import admin

# Register your models here.
from .models import App, Link, Module, Guide

admin.site.register(App)
admin.site.register(Link)
admin.site.register(Module)
admin.site.register(Guide)
