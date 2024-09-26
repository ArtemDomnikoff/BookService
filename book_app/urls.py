from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'signin/', signin),
    path(r'auth/', auth_view),
    path(r'register/', register),
    path(r'registration/', registration),
    path(r'manage/', manage),
    path(r'logout/', logout_view),
]
