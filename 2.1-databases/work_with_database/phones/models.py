from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(max_length=20)
    image = models.ImageField(upload_to='res/')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200, verbose_name=name)

