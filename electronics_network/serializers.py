from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import NetworkNode, Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.

    Метакласс:
    ----------
    fields : list
        Поля, которые будут сериализованы.
    """
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели NetworkNode.

    Метакласс:
    ----------
    fields : list
        Поля, которые будут сериализованы.
    read_only_fields : list
        Поля, доступные только для чтения.
    """
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt', 'created_at')

    def validate_supplier(self, value):
        """
        Проверяет, что поставщик находится на более высоком уровне в иерархии.

        Parameters
        ----------
        value : NetworkNode
            Поставщик для текущего звена.

        Returns
        -------
        NetworkNode
            Валидный объект поставщика.

        Raises
        ------
        serializers.ValidationError
            Если уровень поставщика меньше или равен уровню текущего звена.
        """
        if value and value.level >= self.instance.level:
            raise ValidationError("Поставщик должен быть на более высоком уровне.")
        return value

    def validate_email(self, value):
        """
        Проверяет, что email корректный и содержит символ '@'.

        Parameters
        ----------
        value : str
            Email для валидации.

        Returns
        -------
        str
            Валидированный email.

        Raises
        ------
        serializers.ValidationError
            Если email некорректный.
        """
        if '@' not in value:
            raise serializers.ValidationError("Некорректный email.")
        return value