from rest_framework import routers
from basket.views import BasketViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('basket', viewset=BasketViewSet)
urlpatterns = router.urls
