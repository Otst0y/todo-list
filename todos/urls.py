from django.urls import path

from todos.views import (
    TodosListView,
    TodosCreateView,
    TagListView,
    toggle_complete_or_undo_task,
    TodosUpdateView,
    TodosDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TodosListView.as_view(), name="home"),
    path("create/", TodosCreateView.as_view(), name="todo_create"),
    path("tags/", TagListView.as_view(), name="tags_list"),
    path("tags/create", TagCreateView.as_view(), name="tag_create"),
    path("tags/update/<int:pk>", TagUpdateView.as_view(), name="tag_update"),
    path("tags/delete/<int:pk>", TagDeleteView.as_view(), name="tag_delete"),
    path("toggle/<int:pk>/", toggle_complete_or_undo_task, name="toggle_task"),
    path("update/<int:pk>", TodosUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>/", TodosDeleteView.as_view(), name="todo_delete"),
]

app_name = "todos"
