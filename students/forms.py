from django import forms
from .models import StudentRegister
from django.contrib.auth.models import User

#User creation From for login 
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

#Student Registration Form
class  StudnetRegisterForm(forms.ModelForm):
     class Meta():
         model =  StudentRegister
         fields = ('First_name','Middle_name','last_name','Stu_id',
                   'gender',
                   'Father_name','Standard',)