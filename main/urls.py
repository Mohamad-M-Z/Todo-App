from django.urls import path, include
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.list_planen, name="list-plane" ),
    path('add/', views.AddFormView, name="add"),
    path('delete/<plane_id>',views.delete_plane,name='delete')

]