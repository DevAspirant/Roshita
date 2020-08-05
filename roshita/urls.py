
from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
    path('roshita_list/',views.roshita_list,name='roshita_list'),
    path('update_roshita/<int:pk>/',views.update_roshita,name='update_roshita'),
    path('roshtia_delete/<int:pk>/',views.roshtia_delete,name='roshtia_delete'),
]
