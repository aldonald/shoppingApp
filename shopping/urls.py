"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from server.api.views import ShoppingItemViewSet, AddShoppingItemViewSet, AddItemFromPi
from accounts.api.views import UserViewSet, CreateUserView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# Create our routers
router = routers.DefaultRouter()

# Register the sets router, endpoints for dealing with sets of model instances
router.register(r'shoppingitems', ShoppingItemViewSet, 'shoppingitems')
router.register(r'add_shopping_item', AddShoppingItemViewSet, 'add_shopping_item')
router.register(r'accounts', UserViewSet, 'accounts_api')
# This endpoint to add items to Pi
router.register(r'pi_add_item', AddItemFromPi, 'pi_add_item')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('/', include('server.urls')),
    path('', include('server.urls')),
    url(r'^api/', include((router.urls))),
    url(r'^api-token-auth/', views.obtain_auth_token), # This endpoint to get token
    url(r'^api/create_user', CreateUserView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
