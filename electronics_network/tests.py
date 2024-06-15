from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import NetworkNode


class NetworkNodeModelTest(TestCase):
    """
    Тестовый класс для модели NetworkNode.

    Методы:
    -------
    setUp():
       Устанавливает начальные данные для тестов.
    test_node_creation():
       Проверяет создание объекта NetworkNode.
    test_supplier_validation():
       Проверяет валидацию поставщика на более высоком уровне.
    """
    def setUp(self):
        """
        Устанавливает начальные данные для тестов.

        Создает объект NetworkNode с начальными данными.
        """
        self.node = NetworkNode.objects.create(
            name='Test Factory',
            email='factory@test.com',
            country='Russia',
            city='Moscow',
            street='Test Street',
            house_number='1',
            level=0,
            debt=0.00
        )

    def test_node_creation(self):
        """
        Проверяет создание объекта NetworkNode.

        Убеждается, что атрибуты объекта совпадают с ожидаемыми значениями.
        """
        self.assertEqual(self.node.name, 'Test Factory')
        self.assertEqual(self.node.email, 'factory@test.com')
        self.assertEqual(self.node.country, 'Russia')
        self.assertEqual(self.node.city, 'Moscow')

    def test_supplier_validation(self):
        """
        Проверяет валидацию поставщика на более высоком уровне.

        Убеждается, что создание объекта с поставщиком на том же или более низком уровне вызывает ValidationError.
        """
        with self.assertRaises(ValidationError):
            NetworkNode.objects.create(
                name='Invalid Retailer',
                email='retailer@test.com',
                country='Russia',
                city='Moscow',
                street='Retail Street',
                house_number='2',
                level=1,
                supplier=self.node,
                debt=0.00
            )
