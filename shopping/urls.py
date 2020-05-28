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
from server.api.views import ShoppingItemViewSet, ShoppingListViewSet
from django.conf import settings
from django.conf.urls.static import static

# Create our routers
router = routers.DefaultRouter()

# Register the sets router, endpoints for dealing with sets of model instances
router.register(r'shoppingitems', ShoppingItemViewSet, 'shoppingitems')
router.register(r'shoppinglists', ShoppingListViewSet, 'shoppinglists')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    url(r'^api/', include((router.urls)))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
