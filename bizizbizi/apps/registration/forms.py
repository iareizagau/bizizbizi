from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserCreationFromWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Gehienez 254 karaktere")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email hau dagoeneko erregistratuta dago, saiatu beste batekin.")
        return email


class ProfileForm(forms.ModelForm):
    BOOL_CHOICES = [(True, 'Bai'), (False, 'Ez')]
    public = forms.ChoiceField(choices=BOOL_CHOICES)

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link', 'mountain_club', 'public']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Biografia'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Link'}),
            'mountain_club': forms.TextInput(
                attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Mendiko elkartea'}),
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text='Gehienez 254 karaktere')

    class Meta:
        model = User
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email hau dagoeneko erregistratuta dago, saiatu beste batekin.")
        return email
