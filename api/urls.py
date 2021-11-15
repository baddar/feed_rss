from rest_framework import routers, urlpatterns

from api.views import FeedDataViewSet

router = routers.DefaultRouter()
router.register(r'feed_list', FeedDataViewSet)

urlpatterns = router.urls

