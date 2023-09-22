from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Other URL patterns...
    path('profile/<str:username>/', views.profile_view, name='profile'),
]

