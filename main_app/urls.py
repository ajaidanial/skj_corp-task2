from rest_framework import routers

from .views import PostViewSet, CommentViewSet

router = routers.SimpleRouter()

router.register(r"posts", PostViewSet, basename="post urls")
router.register(r"comments", CommentViewSet, basename="comment urls")

urlpatterns = router.urls
