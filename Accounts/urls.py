from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('user', views.user_view_set)
router.register('feed', views.user_profile_status_view_set)

urlpatterns = [
    path('login/', views.user_login_api_view.as_view()),
    path('', include(router.urls))
]
