from rest_framework import serializers
from basket.models import Basket


class BasketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Basket
        fields = '__all__'
