from rest_framework import routers
from api.user.views import *


router = routers.DefaultRouter()

# router = routers.SimpleRouter()

router.register(r'user', UserViewSet, basename="user")

urlpatterns = router.urls

