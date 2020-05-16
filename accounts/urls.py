from django.urls import path

from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/', views.create_user, name="register"),
    path('', views.user_login),
    path('login/', views.user_login, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
