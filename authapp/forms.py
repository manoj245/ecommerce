import django
from django import forms
from .models import Register
class SignupForm(forms.ModelForm):
    class Meta:
        model=Register
        widgets={'pwd':forms.PasswordInput(),'cpwd': forms.PasswordInput(),}
        fields=['name', 'mobno', 'email', 'username', 'pwd', 'cpwd']
class SigninForm(forms.Form):
    uname = forms.CharField(max_length=10)
    pwd = forms.CharField(max_length=10)
