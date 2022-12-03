from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views

from authentication.views import UserListCreateView, UserDetailUpdateDeleteView, UserAdsDetailView, LocationViewSet, Logout

router = routers.SimpleRouter()
router.register('location', LocationViewSet)

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('<int:pk>/', UserDetailUpdateDeleteView.as_view()),
    path('Z/', UserAdsDetailView.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', Logout.as_view()),
]

urlpatterns += router.urls
