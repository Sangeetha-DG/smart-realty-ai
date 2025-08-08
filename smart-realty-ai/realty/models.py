from django.db import models

# Create your models here.
from django.db import models

class HouseImage(models.Model):
    image = models.ImageField(upload_to='house_images/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
