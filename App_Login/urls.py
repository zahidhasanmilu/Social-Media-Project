from django.urls import path
from .import views


app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('edit_Profile/', views.edit_Profile, name='edit_Profile'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile')
]
