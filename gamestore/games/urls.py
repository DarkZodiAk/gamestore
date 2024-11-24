from rest_framework import routers
from games.views import GamesViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('games', viewset=GamesViewSet)
urlpatterns = router.urls
