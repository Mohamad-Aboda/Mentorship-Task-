from django.urls import path
from .views import task_Create_List, task_Update_Detail_Delete, index 

urlpatterns = [
    path('', index, name='home'),
    path('api/create/', task_Create_List),
    path('api/update/<int:pk>/', task_Update_Detail_Delete),

]
