from django.urls import path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import (
    RegisterView,
    ChangePasswordView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("login/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", RegisterView.as_view(), name='register'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("change-password/", ChangePasswordView.as_view(), name='change-password'),
    # Tasks
    path("tasks/", TaskListView.as_view()),
    path("tasks/create", TaskCreateView.as_view()),
    path('tasks/<int:pk>',TaskUpdateView.as_view()),
    path('tasks/<int:pk>/delete',TaskDeleteView.as_view()),
]
