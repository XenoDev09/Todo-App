from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

from .models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = "todo_app/todo_list.html"
    context_object_name = "todos"


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title"]
    template_name = "todo_app/todo_form.html"
    success_url = reverse_lazy("todo_app:list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "completed"]
    template_name = "todo_app/todo_form.html"
    success_url = reverse_lazy("todo_app:list")


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo_app/todo_confirm_delete.html"
    success_url = reverse_lazy("todo_app:list")


class TodoToggleView(View):
    def post(self, request, pk):
        todo_app = Todo.objects.get(pk=pk)
        todo_app.completed = not todo_app.completed
        todo_app.save(update_fields=["completed"])
        return HttpResponseRedirect(reverse_lazy("todo_app:list"))
