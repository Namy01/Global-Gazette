from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path("post-list/", views.PostListView.as_view(), name="post-list"),
    path("post-by-category/<int:category_id>/", views.PostListByCategory.as_view(), name="post-by-category"),
    path("post-by-tag/<int:tag_id>/", views.PostListByTag.as_view(), name="post-by-tag"),
    path("Post-detail/<int:pk>/", views.PostDetail.as_view(), name="Post-detail"),
    path("post-comment/", views.CommentView.as_view(), name="post-comment"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("post-search/", views.PostSearchView.as_view(), name="post-search"),
    
]