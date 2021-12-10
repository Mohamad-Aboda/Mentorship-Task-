from django.urls import path
from .views import task_Create_List, task_Update_Detail_Delete, change_state

urlpatterns = [
    path('create/', task_Create_List),
    path('update/<int:pk>/', task_Update_Detail_Delete),
    path('change/', change_state), 

]
