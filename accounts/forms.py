from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class RegistrationForm(UserCreationForm):
    age = forms.IntegerField(label='Age')
    email = forms.EmailField(label='Email Address')
    gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES, required=False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ['username','email', 'password1', 'password2','first_name', 'last_name', 'age','gender']
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 13:
            raise forms.ValidationError(_("You must be of thirteen years of age to register"))
        return age
    def clean_email(self):
        data = self.cleaned_data['email']
        if CustomUser.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use')
        return data

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'bio', 'age', 'gender')
class CustomUserCreationForm(UserCreationForm):
    age= forms.IntegerField(label='Age')
    class Meta(UserCreationForm.Meta):
        model = CustomUser
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 13:
            raise forms.ValidationError(_("You must be of thirteen years of age to register."))
        return age 
       

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
