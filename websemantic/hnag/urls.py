from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("posts", views.posts, name="posts"),
    path("search", views.search, name="search"),
    path("loadSubMenu", views.loadSubMenu, name="loadSubMenu")
]