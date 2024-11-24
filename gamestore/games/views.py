from rest_framework.permissions import IsAuthenticated
from .models import Games
from .serializers import GamesSerializer
from rest_framework.viewsets import ModelViewSet

class GamesViewSet(ModelViewSet):
    serializer_class = GamesSerializer
    queryset = Games.objects.all()

    def get_queryset(self):
        return Games.objects.all()
