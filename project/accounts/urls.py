from django.urls import path, include
from .views import MyPageView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('mypage/', MyPageView.as_view(), name='mypage'),
    path('', include('dj_rest_auth.urls')),
    path('join/', include('dj_rest_auth.registration.urls')),  # User registration
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Token obtain
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT Token refresh
]
