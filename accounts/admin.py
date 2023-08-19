from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
admin.site.register(CustomUser, add_form=CustomUserCreationForm)



