from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('testing-viewset', views.TestViewSet, base_name='testing-viewset') # only specify queryset if you don't have a queryset on ViewSet or you want to override the name associated with the queryset
router.register('profile', views.UserProfileViewSet) # don't need base_name because a queryset was provided

urlpatterns = [
    path('testing-apiview/', views.TestView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
