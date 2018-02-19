from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import home, open_list, add_item, delete_item, add_list, SignUpView

urlpatterns = [

    path('home', home, name="user_home_page"),
    path('home/<int:list_id>', open_list, name="list_page"),

    path('item/<int:list_id>', add_item, name="add_item"),
    path('item/delete/<int:item_id>/<int:list_id>', delete_item, name="delete_item"),

    path('list/<int:list_id>', add_list, name="add_list"),

    path('login',
         LoginView.as_view(template_name="app/login_form.html"),
         name="login"),
    path('logout', LogoutView.as_view(),name="logout"),

    path('signup', SignUpView.as_view(), name='signup')

]
