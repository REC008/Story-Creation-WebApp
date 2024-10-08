# story_creator/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    home,
    StoryViewSet,
    ContributionViewSet,
    UserRegistrationView,
    CurrentUserView,
    ExpiredTokenRefreshView,
    LogoutView,
    UserLoginView,
    story_contributions,
)

# Initialize the router and register view sets
router = DefaultRouter()
router.register(r'stories', StoryViewSet)
router.register(r'contributions', ContributionViewSet)

# Define urlpatterns for the app
urlpatterns = [  # Make sure this variable is named urlpatterns
    path('', home, name='home'),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path('refresh/', ExpiredTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("current-user/", CurrentUserView.as_view(), name="current_user"),
    path('story/<int:pk>/contributions/', story_contributions, name='story-contributions'),
    path("api/", include(router.urls)),  # Include the router URLs for the API
]