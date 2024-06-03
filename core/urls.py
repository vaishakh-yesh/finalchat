from django.contrib.auth import views as auth_auth
from django.urls import path
from . import views

urlpatterns = [
    path('',views.frontpage,name='frontpage'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_auth.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('logout/',auth_auth.LogoutView.as_view(),name='logout'),
]