from django.urls import path, include

from rest_framework import routers

from .views import CategoryMVS, PostViewsMVS,CommentMVS

# defualt rotuer classından rotuer objeesi oluşturldu.
router = routers.DefaultRouter()
router.register("category", CategoryMVS)
router.register("post", PostViewsMVS)
router.register("comment", CommentMVS)


urlpatterns = [
    path('',include(router.urls))
]


