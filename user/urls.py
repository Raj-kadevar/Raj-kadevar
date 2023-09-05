from django.urls import path

from user.views import UserView, UserDetail

urlpatterns = [
    path("", UserView.as_view(), name="index"),
    path("user/", UserDetail.as_view(), name="user")
]