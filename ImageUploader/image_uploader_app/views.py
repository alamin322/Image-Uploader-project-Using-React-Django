from django.shortcuts import render
from image_uploader_app.models import Image
from image_uploader_app.serializers import ImageUploaderSerializer
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)


# Create your views here.
class ImageList(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageUploaderSerializer


class ImageCreate(CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageUploaderSerializer


class ImageRetrieve(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageUploaderSerializer
    lookup_field = 'pk'


class ImageDestroy(DestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageUploaderSerializer
    lookup_field = 'id'


class ImageUpdate(UpdateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageUploaderSerializer
    lookup_field = 'id'
