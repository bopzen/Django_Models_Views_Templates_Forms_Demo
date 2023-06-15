from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from models_demo.hr.models import Employee, Username, Image, ToDoList
from models_demo.hr.validators import validate_symbols, ValueInRangeValidator


class ToDoListForm(forms.Form):
    task = forms.CharField(
        validators=(validate_symbols,),
        max_length=100
    )
    complete = forms.BooleanField(required=False)
    priority = forms.IntegerField(validators=(
        ValueInRangeValidator(1, 10),
    ))


class ToDoListModelForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = '__all__'
        
    def clean(self):
        return super().clean()
    
    def clean_task(self):
        return self.cleaned_data['task'].lower()

    def clean_priority(self):
        priority = self.cleaned_data['priority']
        if priority == 5:
            raise ValidationError(f"Priority cannot be {priority}")
        return priority


class TestForm(forms.Form):

    CHOICES = (
        ('1', 'Junior'),
        ('2', 'Mid'),
        ('3', 'Senior'),
    )
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField(min_value=0, max_value=200)
    email = forms.EmailField(required=False)
    url = forms.URLField(initial='https://')
    comment = forms.CharField(widget=forms.Textarea)
    level = forms.CharField(widget=forms.Select(choices=CHOICES))
    is_full_time = forms.BooleanField(label='Full time')
    level_radio = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['slug']


class UsernameForm(forms.ModelForm):
    class Meta:
        model = Username
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'