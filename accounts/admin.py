from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username']


admin.site.register(User, CustomUserAdmin)
