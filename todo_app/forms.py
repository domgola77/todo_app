from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Wpisz tytuł zadania'}),
            'priority': forms.Select(attrs={'class': 'priority-select'}),
        }
