from django.core.exceptions import ValidationError
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class NetworkNode(models.Model):
    """
    Модель NetworkNode представляет звено в сети по продаже электроники.

    Атрибуты:
    ----------
    name : str
        Название звена сети.
    email : str
        Email для контактов.
    country : str
        Страна расположения.
    city : str
        Город расположения.
    street : str
        Улица расположения.
    house_number : str
        Номер дома.
    level : int
        Уровень в иерархии (0 - Завод, 1 - Розничная сеть, 2 - Индивидуальный предприниматель).
    supplier : NetworkNode
        Поставщик оборудования для данного звена сети.
    debt : Decimal
        Задолженность перед поставщиком.
    created_at : datetime
        Время создания объекта.
    """
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    level = models.IntegerField(choices=LEVEL_CHOICES)
    supplier = models.ForeignKey('self', **NULLABLE, on_delete=models.SET_NULL)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def clean(self):
        """
        Проверяет, что поставщик находится на более высоком уровне в иерархии.

        Raises
        ------
        ValidationError
            Если уровень поставщика меньше или равен уровню текущего звена.
        """
        if self.supplier and self.supplier.level >= self.level:
            raise ValidationError("Поставщик должен быть на более высоком уровне.")


class Product(models.Model):
    """
    Модель Product представляет продукт, который продается через сеть.

    Атрибуты:
    ----------
    name : str
        Название продукта.
    model : str
        Модель продукта.
    release_date : date
        Дата выхода продукта на рынок.
    network_node : NetworkNode
        Звено сети, продающее данный продукт.
    """
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=100)
    release_date = models.DateField()
    network_node = models.ForeignKey(NetworkNode, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
