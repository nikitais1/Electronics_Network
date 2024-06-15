# views.py
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import NetworkNode
from .serializers import NetworkNodeSerializer


class IsActiveEmployee(permissions.BasePermission):
    """
    Класс для проверки, что пользователь является активным сотрудником.
    """
    def has_permission(self, request, view):
        """
        Проверяет, что пользователь аутентифицирован и активен.

        Parameters
        ----------
        request : HttpRequest
            Текущий запрос.
        view : View
            Текущая вьюшка.

        Returns
        -------
        bool
            True, если пользователь аутентифицирован и активен, иначе False.
        """
        return request.user and request.user.is_authenticated and request.user.is_active


class NetworkNodeViewSet(viewsets.ModelViewSet):
    """
    Представление для модели NetworkNode с CRUD операциями.

    Атрибуты:
    ----------
    queryset : QuerySet
        Запрос для получения объектов NetworkNode.
    serializer_class : Serializer
        Класс сериализатора для объектов NetworkNode.
    permission_classes : list
        Список классов разрешений.
    filter_backends : list
        Список классов для фильтрации запросов.
    filterset_fields : list
        Поля для фильтрации.
    search_fields : list
        Поля для поиска.
    ordering_fields : list
        Поля для сортировки.
    """
    queryset = NetworkNode.objects.all().select_related('supplier').prefetch_related('products')
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsAuthenticated, IsActiveEmployee]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['country', 'city']
    search_fields = ['name', 'city', 'email']
    ordering_fields = ['name', 'created_at']


