from django.urls import path
from .views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoToggleView

app_name = "todo_app"

urlpatterns = [
    path("", TodoListView.as_view(), name="list"),
    path("new/", TodoCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", TodoUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", TodoDeleteView.as_view(), name="delete"),
    path("<int:pk>/toggle/", TodoToggleView.as_view(), name="toggle"),
]