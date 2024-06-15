from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import NetworkNode, Product


class NetworkNodeAdmin(admin.ModelAdmin):
    """
    Класс для управления объектами модели NetworkNode в админ-панели.

    Методы:
    -------
    supplier_link(obj):
        Возвращает ссылку на поставщика.
    clear_debt(request, queryset):
        Очищает задолженность перед поставщиком для выбранных объектов.
    """
    list_display = ('name', 'city', 'supplier', 'debt', 'created_at')
    list_filter = ('city',)
    search_fields = ('name',)

    def supplier_link(self, obj):
        """
        Возвращает HTML-ссылку на поставщика.

        Parameters
        ----------
        obj : NetworkNode
            Текущий объект NetworkNode.

        Returns
        -------
        str
            HTML-ссылка на объект поставщика.
        """
        if obj.supplier:
            link = reverse('admin:network_networknode_change', args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', link, obj.supplier.name)
        return 'None'

    supplier_link.allow_tags = True
    supplier_link.short_description = 'Поставщик'

    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        """
        Действие для очистки задолженности перед поставщиком для выбранных объектов.

        Parameters
        ----------
        request : HttpRequest
            Текущий запрос.
        queryset : QuerySet
            Выбранные объекты.
        """
        queryset.update(debt=0.00)
        self.message_user(request, "Задолженность успешно очищена.")
    clear_debt.short_description = 'Очистить задолженность перед поставщиком'


admin.site.register(NetworkNode, NetworkNodeAdmin)
admin.site.register(Product)
