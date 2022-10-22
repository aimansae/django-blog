from . import views
from django.urls import path

urlpatterns = [
    # as view because we are using class based urls
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("like/<slug:slug>/", views.PostLike.as_view(), name="post_like"),
]
