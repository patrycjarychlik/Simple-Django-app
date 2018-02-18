from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import home, open_list

urlpatterns = [

    path('home', home, name="user_page"),
    path('home/<int:list_id>', open_list, name="list_page"),

    path('login',
         LoginView.as_view(template_name="ui/login_form.html"),
         name="login"),

    path('logout',
         LogoutView.as_view(),
         name="logout")

]
