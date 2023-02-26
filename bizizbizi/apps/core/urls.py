from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('detail_spot/<pk>/', views.PostDetailView.as_view(), name='detail_spot'),
    path('detail_travel/<pk>/', views.TravelDetailView.as_view(), name='detail_travel'),
    path('api_get/', views.GpsTrackingApiView.as_view(), name='api_get'),
    path('api_post/', views.GpsTrackingView, name='api_post'),
    path('realtime/', views.realtime, name='realtime'),
    path('travels/', views.travels, name="travels"),
    path('', views.index, name="home"),

]

