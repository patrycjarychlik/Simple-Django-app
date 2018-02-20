from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import home, open_list, add_item, delete_item, add_list, SignUpView, add_service, add_category, \
    delete_service, open_money, money, delete_list, delete_category, mark_done, edit_budget

urlpatterns = [

    path('home', home, name="user_home_page"),
    path('home/<int:list_id>', open_list, name="list_page"),

    path('item/<int:list_id>', add_item, name="add_item"),
    path('item/delete/<int:item_id>/<int:list_id>', delete_item, name="delete_item"),
    path('item/mark/<int:item_id>/<int:list_id>', mark_done, name="mark_done"),

    path('list/delete/<int:list_id>', delete_list, name="delete_list"),
    path('list/<int:list_id>', add_list, name="add_list"),

    path('budget/<int:list_id>', edit_budget, name="edit_budget"),



    path('money', money, name="user_money_page"),
    path('money/<int:list_id>', open_money, name="list_category"),

    path('service/<int:list_id>', add_service, name="add_service"),
    path('service/delete/<int:item_id>/<int:list_id>', delete_service, name="delete_service"),

    path('category/delete/<int:list_id>', delete_category, name="delete_category"),
    path('category/<int:list_id>', add_category, name="add_category"),

    path('login',
         LoginView.as_view(template_name="app/login_form.html"),
         name="login"),
    path('logout', LogoutView.as_view(),name="logout"),

    path('signup', SignUpView.as_view(), name='signup')

]

