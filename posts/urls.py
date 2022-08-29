from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("post_create/", views.post_create, name="post_create"),
    path("post_update/<str:pk>/", views.post_update, name="post_update"),
    path("post_delete/<str:pk>/", views.post_delete, name="post_delete"),
]