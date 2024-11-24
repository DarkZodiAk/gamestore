from rest_framework import serializers
from wishlist.models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Wishlist
        fields = '__all__'
