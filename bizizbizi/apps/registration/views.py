from .forms import UserCreationFromWithEmail, ProfileForm, EmailForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFromWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Repite la contraseña'})
        return form


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profiles')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def get_context_data(self, **kwargs):
        print(f"**registration.view** \n user {self.request.user} id {self.request.user.id} type {type([self.request.user.id])}")
        print("**HELLO**")

        profiles_visibles = Profile.objects.filter(public=True).values_list('id', flat=True)
        all_users = User.objects.values_list('username', flat=True)
        print(f"all_users {list(all_users)}")
        print(f"profiles_visibles {list(profiles_visibles)}")

        context = super(ProfileUpdate, self).get_context_data(**kwargs)
        print("context\n", context)
        # context['climbingspot'] = ClimbingSpot.objects.filter(user=context['profile'])
        # context['climbingspot'] = ClimbingSpot.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profiles')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        return form
