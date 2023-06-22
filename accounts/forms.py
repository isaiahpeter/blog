from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class RegistrationForm(UserCreationForm):
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES, required=False)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'age','gender')
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
