from django import forms 


class TaskForm(forms.Form):
    title = forms.CharField(max_length=250, label="Task Title")
    descriptton = forms.CharField(widget=forms.Textarea)
    due_date = forms.DateField(widget=forms.SelectDateWidget)