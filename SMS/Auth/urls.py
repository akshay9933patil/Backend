from django.urls import path
from .views import CreateUserView, LoginView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('create-user/',CreateUserView.as_view()),
    path('access/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',LogoutView.as_view()),
]