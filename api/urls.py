from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path("posts/", views.posts),
    path("posts/<str:pk>/", views.post),
    path("posts/users/<str:pk>/", views.posts_user),
]