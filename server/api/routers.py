from rest_framework import routers

# Create our routers
# Apps need to register any routes with each router, eg:
# `v2router.register(r'foo', FooViewSet, basename='foo')`
router = routers.DefaultRouter()

# Register the sets router, endpoints for dealing with sets of model instances
# router.register()
