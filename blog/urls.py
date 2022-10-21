from . import views
from django.urls import path

urlpatterns = [
    #as view because we are using class based urls
    path("", views.PostList.as_view(), name="home"),
]