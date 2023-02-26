from django.urls import path
from .views import SignUpView, ProfileUpdate, EmailUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profiles/', ProfileUpdate.as_view(), name='profiles'),
    path('profiles/email/', EmailUpdate.as_view(), name='profile_email'),
]