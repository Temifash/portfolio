from django.urls import path
from . import views

urlpatterns = [
    # path("", views.blogHome, name="blogHome"),
    # path("blogDetails/", views.blogDetails, name="blogDetails"),
    # path("addBlog/", views.addBlog, name="addBlog"),

    path("", views.blogHome, name="blogHome"),
    path("new/", views.blogNew, name="blogNew"),
    path("<int:pk>/", views.blogDetails, name="blogDetails"),
    path("delete/<int:id>/", views.deleteBlog, name="deleteBlog"),
]
