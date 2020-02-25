from django.contrib import admin
from django.urls import path
from todo.views import index, regist, detail, edit, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', index),
    path('todo/regist/', regist),
    path('todo/detail/<int:pk>/', detail),
    path('todo/edit/', edit),
    path('todo/delete/', delete),
]