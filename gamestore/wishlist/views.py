from rest_framework.permissions import IsAuthenticated
from .models import Wishlist
from .serializers import WishlistSerializer
from rest_framework.viewsets import ModelViewSet


class WishlistViewSet(ModelViewSet):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Wishlist.objects.all()
        else:
            return Wishlist.objects.filter(user=self.request.user)
