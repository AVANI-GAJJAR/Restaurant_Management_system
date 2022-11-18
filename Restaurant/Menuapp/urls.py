from django import views
from django.contrib import admin
from django.urls import path
from Menuapp import views
urlpatterns = [
    path('', views.index,name="index"),
    path('index', views.index,name="index"),
    path('add', views.add,name="add"),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('show', views.show,name="show"),
    #path('update', views.update,name="update"),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    #path('delete', views.delete,name="delete"),
    path('delete/<int:id>', views.delete, name='delete'),
]