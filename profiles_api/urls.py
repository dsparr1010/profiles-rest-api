from django.urls import path
from profiles_api import views

urlpatterns = [
    path('testing-view/', views.TestView.as_view()),
]
