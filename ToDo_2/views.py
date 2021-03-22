from rest_framework import viewsets
from .models import User, Todo
from .serializers import TodoSerializer, UserSerializer

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # filter_fields先がリレーションのあるテーブルだった場合はpk打ち込みで検索
    filter_fields = ('user', 'title')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
