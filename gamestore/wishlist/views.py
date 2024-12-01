from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
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

    # Удалить игру из корзины
    @action(detail=False, methods=['delete'], url_path='remove_game/(?P<game_id>[^/.]+)',
            permission_classes=[IsAuthenticated])
    def remove_game(self, request, game_id=None):
        deleted_count, _ = Wishlist.objects.filter(user=request.user, game_id=game_id).delete()
        if deleted_count > 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "No items found for this game."}, status=status.HTTP_404_NOT_FOUND)

    # @action(detail=False, methods=['delete'], permission_classes=[IsAuthenticated])
    # def remove_game(self, request):
    #     game_id = request.data.get('game_id')
    #
    #     if game_id is None:
    #         return Response({"detail": "Game ID must be provided."}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     Wishlist.objects.filter(user=request.user, game=game_id).delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
