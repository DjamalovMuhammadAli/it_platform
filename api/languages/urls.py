from rest_framework import routers
from api.languages.views import *

router = routers.DefaultRouter()

router.register(r'language', LanguageViewSet, basename="language")

urlpatterns = router.urls
