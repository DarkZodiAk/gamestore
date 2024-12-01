from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
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

    #Грохнуть всю корзину пользователя :)
    @action(detail=False, methods=['delete'], permission_classes=[IsAuthenticated])
    def clear(self, request):
        Basket.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    #Удалить игру из корзины
    @action(detail=False, methods=['delete'], url_path='remove_game/(?P<game_id>[^/.]+)',
            permission_classes=[IsAuthenticated])
    def remove_game(self, request, game_id=None):
        deleted_count, _ = Basket.objects.filter(user=request.user, game_id=game_id).delete()
        if deleted_count > 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "No items found for this game."}, status=status.HTTP_404_NOT_FOUND)

    #Получить число игр в корзине
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def count(self, request):
        count = Basket.objects.filter(user=request.user).count()
        return Response({'count': count}, status=status.HTTP_200_OK)