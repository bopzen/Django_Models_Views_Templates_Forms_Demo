from django import forms
from models_demo.hr.models import Employee, Username, Image


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