from rest_framework import serializers
from image_uploader_app.models import Image

class ImageUploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'