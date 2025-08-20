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


class TodoCreateForm(forms.ModelForm):
    deadline = forms.CharField(initial="2020-12-12 12:00")
    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]
        widgets = {
            "deadline": forms.DateTimeInput(),
            "tags": forms.CheckboxSelectMultiple()
        }
