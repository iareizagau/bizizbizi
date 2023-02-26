from django.urls import path
from .views import ProfileListView, ProfileDetailView, ProfileCreateSpotFormView
from . import views

profiles_patterns = ([
    path('', ProfileListView.as_view(), name='list'),
    path('create', ProfileCreateSpotFormView.as_view(), name='create_new'),
    path('<username>/detail', ProfileDetailView.as_view(), name='detail'),
    path('detail_view/<pk>/', views.PostDetailView.as_view(), name='detail_spot'),
    path('edit_spot/<pk>/', views.EditPostDetailView.as_view(), name='edit_spot'),
    ], "profiles")
