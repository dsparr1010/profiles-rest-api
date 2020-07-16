from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('testing-viewset', views.TestViewSet, base_name='testing-viewset')

urlpatterns = [
    path('testing-apiview/', views.TestView.as_view()),
    path('', include(router.urls))
]
