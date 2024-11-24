from rest_framework.permissions import IsAuthenticated
from .models import Basket
from .serializers import BasketSerializer
from rest_framework.viewsets import ModelViewSet


class BasketViewSet(ModelViewSet):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Basket.objects.all()
        else:
            return Basket.objects.filter(user=self.request.user)
