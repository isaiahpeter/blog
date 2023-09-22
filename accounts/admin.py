from django.contrib import admin
from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
admin.site.register(CustomUser, add_form=CustomUserCreationForm)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'profile_picture', 'bio']
    raw_id_fields = ['user']

