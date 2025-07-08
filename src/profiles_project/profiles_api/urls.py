from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewset, basename='hello-viewset')
router.register('profile', views.UserprofileViewSet)
router.register('login', views.LoginViewSet, basename='login')
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns= [

    path('hello-view/', views.HelloApiView.as_view()),
    path('',include(router.urls))
]