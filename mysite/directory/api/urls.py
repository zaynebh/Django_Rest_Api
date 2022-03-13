from rest_framework.routers import DefaultRouter
from directory.api.views import UsersViewSet,CompanyViewSet, UserSearchViewSet

router = DefaultRouter(
    trailing_slash=False,
)
router.register(
    'users/', UsersViewSet, basename='users',
  
  
)
router.register(
  
    'company/$', CompanyViewSet, basename='company',
   
)
router.register(
  
    '^users/$', UserSearchViewSet, basename='"user_search',
   
)

urlpatterns = router.urls
