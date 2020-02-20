from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register("name", views.viewset)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/registration/", views.CreateUserView.as_view(), name='registration'),
]