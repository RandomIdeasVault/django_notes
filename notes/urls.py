from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='base'),
    path('apps/', views.AppView.as_view(), name='apps'),
    path('modules/', views.ModuleView.as_view(), name='modules'),
    path('links/', views.LinkView.as_view(), name='links'),
    path('guides/', views.GuideView.as_view(), name='guides'),
]
