from django.urls import path, include


urlpatterns = [
    path('todo/', include('dwa_todo.urls')),
]