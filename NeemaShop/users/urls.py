from django.urls import path
from .views import (
    UpdateUserView,
    UserListView,
    UserDetailView,
    RegisterView,
    LoginView,
    UpdateUserView,
    ChangePasswordView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<str:email>/', UserDetailView.as_view(), name='user-detail'),
    path('update-user/', UpdateUserView.as_view(), name='update-user'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
