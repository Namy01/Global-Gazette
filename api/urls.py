from django.urls import path, include
from . import views
from rest_framework import routers  # type: ignore

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'categories', views.CategoryViewSet)



urlpatterns = [
    path('', include(router.urls)),
    
    
]