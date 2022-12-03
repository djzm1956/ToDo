from django import forms
from .models import ToDos
from .models import SearchTerms


class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchTerms
        fields = '__all__'

        widgets = {
            'search': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Search tasks'})
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDos
        fields = '__all__'

        widgets = {
            'task': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Add a new task'})
        }
