from django import forms

from todos.models import Task


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]
        widgets = {
            "deadline": forms.DateTimeInput(),
            "tags": forms.CheckboxSelectMultiple()
        }
