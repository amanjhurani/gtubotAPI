from django.urls import include, path
from rest_framework import routers
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/get_post_list', views.get_post_list, name="posts_list"),
    path('api/v1/create_post', views.create_post, name="create_post`"),
]