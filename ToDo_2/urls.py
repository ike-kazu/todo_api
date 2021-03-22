from rest_framework import routers
from .views import UserViewSet, TodoViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='Users')
router.register(r'todos', TodoViewSet, basename='Todos')
