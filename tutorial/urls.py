from django.urls import path

from .views import UserView, UserView2

urlpatterns = [
    path('', UserView.as_view()),
    path('2', UserView2.as_view()),
]
