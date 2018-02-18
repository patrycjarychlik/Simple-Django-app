from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import home

urlpatterns = [

    path('home', home, name="user_page"),

    path('login',
         LoginView.as_view(template_name="interface/login_form.html"),
         name="login"),

    path('logout',
         LogoutView.as_view(),
         name="logout")

]
