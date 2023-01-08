from django.urls import path
from . import views


urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('register/',views.register.as_view(),name='register'),
]