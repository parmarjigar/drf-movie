from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import MediaFile
from .serializers import UploadMediaSerializer, GetMediaSerializer


class UploadMediaAPI(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UploadMediaSerializer
    queryset = MediaFile.objects.all()


class GetMediaAPI(RetrieveAPIView):
    queryset = MediaFile.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = GetMediaSerializer
