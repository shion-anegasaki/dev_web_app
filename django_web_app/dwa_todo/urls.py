from django.urls import path
from dwa_todo.views import index, regist, detail, edit, delete


app_name = 'todo'
urlpatterns = [
    path('', index),
    path('regist/', regist),
    path('detail/<int:pk>/', detail),
    path('edit/', edit),
    path('delete/', delete),
]