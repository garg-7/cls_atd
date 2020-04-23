from django.db import models


class ClassImage(models.Model):
    upload_image = models.ImageField(upload_to='class/')
