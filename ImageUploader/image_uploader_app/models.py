from django.db import models
from PIL import Image as myimg


# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    # comment: User Profile Image resize Function
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = myimg.open(self.image.path)
        if img.height > 600 or img.width > 600:
            output_size = (400, 400)
            img.thumbnail(size=output_size)
            img.save(self.image.path)