from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from todos.forms import TodoUpdateForm
from todos.models import Task, Tag


class TodosListView(generic.ListView):
    model = Task
    template_name = "todos/home.html"


class TodosCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "is_done", "tags"]
    success_url = reverse_lazy("todos:home")
    template_name = "todos/task_create.html"

    initial = {
        "deadline": "2020-12-12 12:00"
    }


class TodosUpdateView(generic.UpdateView):
    model = Task
    form_class = TodoUpdateForm
    success_url = reverse_lazy("todos:home")
    template_name = "todos/task_update.html"


class TodosDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todos:home")
    template_name = "todos/task_delete.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "todos/tags_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todos:tags_list")
    template_name = "todos/tag_create.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todos:tags_list")
    template_name = "todos/tag_update.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todos:tags_list")
    template_name = "todos/tag_delete.html"


def toggle_complete_or_undo_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True
    task.save()
    return redirect("todos:home")
