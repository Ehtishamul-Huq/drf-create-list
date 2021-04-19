from django.urls import path
from .views import UserView, UserListView
from django.urls import path

urlpatterns = [
    path('create/', UserView.as_view()),
    path('list/', UserListView.as_view()),
]