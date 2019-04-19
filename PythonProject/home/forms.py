from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Images

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddImageForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'size':80}))
    class Meta:
        model = Images
        fields = '__all__'
