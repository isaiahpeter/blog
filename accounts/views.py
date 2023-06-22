from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import ProfileForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            age = form.cleaned_date.get('age')
            if age is not None and age < 13:
                form.add_error('age', 'You must be at least thirteen years old to register.')
            else:
                user.save()
                login(request, user)
                return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form':form})           

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(requesr, user)
            return redirect('home')
    else:
        form = AuthenticationForm(request)
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form': form})
