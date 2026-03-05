from django import forms

class CreateTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.Textarea()