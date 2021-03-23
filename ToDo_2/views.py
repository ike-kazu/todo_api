from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from .models import User, Todo
from .serializers import TodoSerializer, UserSerializer

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    # filter_fields先がリレーションのあるテーブルだった場合はpk打ち込みで検索
    filter_fields = ('user', 'title')

    def get_queryset(self):
        if self.request.method in SAFE_METHODS:
            return Todo.objects.filter(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
