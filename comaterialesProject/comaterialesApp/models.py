from io import BytesIO
from PIL import Image

from django.db import models
from django.core.files import File

class Categoria(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SliceField()

    def __str__(self):
        return self.name   

    def get_absolute_url(self):
        return f'/{self.slug}/' 

class Producto (models.Model):
    category = models.ForeignKey(Categoria, related_name='productos')