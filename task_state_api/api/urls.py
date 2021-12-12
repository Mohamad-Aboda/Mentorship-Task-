from django.urls import path
from .views import task_create_list, task_update_detail_delete, index 

urlpatterns = [
    path('', index, name='home'),
    path('api/tasks/', task_create_list, name='create_list'),
    path('api/tasks/<int:pk>/', task_update_detail_delete, name ='update_detail_delete'),

]
