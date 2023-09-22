from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Profile
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse

@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(View):
    template_name = 'profile_update.html'  # Define the template for rendering the update form

    def get(self, request):
        # Get the current user's profile
        user_profile = Profile.objects.get(user=request.user)

        # Create an instance of the profile update form with the current profile data
        form = ProfileForm(instance=user_profile)

        context = {
            'form': form,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        # Get the current user's profile
        user_profile = Profile.objects.get(user=request.user)

        # Create an instance of the profile update form with the POST data
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            # Save the updated profile data
            form.save()
            return redirect('profile_detail')  # Redirect to the profile detail view
        else:
            context = {
                'form': form,
            }
            return render(request, self.template_name, context)



def profile_view(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'accounts/profile.html', { 'profile': profile})
