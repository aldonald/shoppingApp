from django.urls import path
from server.views import IndexView

app_name = 'server'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
