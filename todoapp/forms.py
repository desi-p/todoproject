from django import forms
from .models import Mytodo

#form class - import class Mytodo/tasks
class TodoForm(forms.ModelForm):
    class Meta:
        model = Mytodo
        fields = ['task'] #as list of all attributes of Mytodo Class in models.py 
        