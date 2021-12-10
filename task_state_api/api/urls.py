from django.urls import path
from .views import * 

urlpatterns = [
    path('', index, name='index'), 
    path('all/', taskList, name = 'taskList'),
    path('create/', taskCreate, name='taskCreate'), 
    path('details/<int:pk>/', taskDetail, name = 'taskList'), 
    path('delete/<int:pk>/', taskDetail, name = 'taskDelete'), 
    path('update/<int:pk>/', taskDetail, name = 'taskUpdate'), 


]
