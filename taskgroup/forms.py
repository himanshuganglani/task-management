from django import forms
from django.core.exceptions import ValidationError
from .models import User,TaskModel


class RegisterForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True)
	password2 = forms.CharField(required=True)
	class Meta:
		model = User
		fields = ('email','password')
		widgets = {
		'email': forms.TextInput({'autocomplete': 'off',}),
        'password': forms.PasswordInput(),

		}
class LoginForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User

		fields = ('email','password')
		widgets = {
        'password': forms.PasswordInput(),
		}

class TaskForm(forms.ModelForm):
	Name = forms.CharField(required=True)
	Description = forms.CharField(required=True)
	StartTime = forms.DateField(required=True)
	EndTime = forms.DateField(required=True)
	Status = forms.CharField(required=True)
	
	class Meta:
		model = TaskModel
		fields = '__all__'
		widgets = {
		'Name': forms.TextInput({'autocomplete': 'off',}),
		'Description': forms.Textarea({'autocomplete': 'off',}),
		'StartTime': forms.DateInput({'autocomplete': 'off',format :"%m/%d/%Y"}),
		'EndTime': forms.DateInput({'autocomplete': 'off',format :"%m/%d/%Y"}),
		'Status': forms.TextInput({'autocomplete': 'off',})
        }


"""	def save(self, commit=True):
  		user = super(RegisterForm, self).save(commit=False)
  		user.email = self.cleaned_data ['email'] 
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            """
            