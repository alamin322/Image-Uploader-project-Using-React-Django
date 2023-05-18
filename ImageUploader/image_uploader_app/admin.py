from django.contrib import admin
from image_uploader_app.models import Image

# Register your models here.
@admin.register(Image)
class ImageUploaderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'uploaded_at')