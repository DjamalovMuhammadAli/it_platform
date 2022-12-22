from xcore.router import DefaultRouter

from api.user.urls import router as user_router
from api.languages.urls import router as languages_router

router = DefaultRouter()
router.extend(user_router)
router.extend(languages_router)
