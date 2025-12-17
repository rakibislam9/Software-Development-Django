from django import forms 
from tasks.models import Task, TaskDetails


class TaskForm(forms.Form):
    title = forms.CharField(max_length=250, label="Task Title")
    description = forms.CharField(widget=forms.Textarea)
    due_date = forms.DateField(widget=forms.SelectDateWidget)
    assigned_to = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, 
        choices = [])

    def __init__(self, *args, **kwargs):
        employees = kwargs.pop("employees", [])
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].choices = [
            (emp.id, emp.name) for emp in employees
        ]


class StyledFormmixin:
    """Mixing to apply style to form filed"""

    default_classes = "border border-gray-300 w-1/2 rounded-lg shadow-sm focus:border-rose-500 focus:ring-rose-500",


    def apply_styled_widgets(self):
        for field_name, fields in self.fields.items():
            if isinstance(fields.widget, forms.TextInput):
                fields.widget.attrs.update({
                    'class' : self.default_classes,
                    'placeholder': f"Enter {fields.label.lower()}"
                })
            elif isinstance(fields.widget, forms.Textarea):
                fields.widget.attrs.update({
                    'class' : f'{self.default_classes} resize-none',
                    'placeholder': f"Enter {fields.label.lower()}",
                    'rows': 4
                })
            elif isinstance(fields.widget, forms.SelectDateWidget):
                
                fields.widget.attrs.update({
                    'class' : "border border-gray-300 rounded-lg shadow-sm focus:border-rose-500 focus:ring-rose-500",
                })
            elif isinstance (fields.widget, forms.CheckboxSelectMultiple):
               
                fields.widget.attrs.update({
                    'class' : "space-y-2"
                })
            else:
                fields.widget.attrs.update({
                    'class' : self.default_classes
                })


class TaskModelForm(StyledFormmixin, forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to']
        widgets = {
            'due_date' : forms.SelectDateWidget,
            'assigned_to' : forms.CheckboxSelectMultiple
        }
        '''Using Mixing widget'''



        '''manualbwudget'''
        

    '''widget use Mixing'''

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.apply_styled_widgets()

    
class TaskDetaileModeleForm(StyledFormmixin,forms.ModelForm):
    class Meta:
      model = TaskDetails
      fields = ['priority', 'notes']

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.apply_styled_widgets()
