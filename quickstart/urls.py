from django.urls import path, include

from .api import UploadMediaAPI, GetMediaAPI

app_label = "media"

urlpatterns = [
    path('upload/', UploadMediaAPI.as_view(), name="upload_media"),
    path('get/movie/<int:pk>', GetMediaAPI.as_view(), name="upload_media")
]