from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from server.api.views import ShoppingItemViewSet, ShoppingListViewSet

# Create our routers
# Apps need to register any routes with each router, eg:
router = routers.DefaultRouter()

# Register the sets router, endpoints for dealing with sets of model instances
router.register(r'shoppingitems', ShoppingItemViewSet, 'shoppingitems')
router.register(r'shoppinglists', ShoppingListViewSet, 'shoppinglists')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include((router.urls))),
]
