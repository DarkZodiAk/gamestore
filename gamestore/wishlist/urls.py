from rest_framework import routers
from wishlist.views import WishlistViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('wishlist', viewset=WishlistViewSet)
urlpatterns = router.urls
