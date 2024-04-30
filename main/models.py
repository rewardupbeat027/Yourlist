from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/')


class Purchase(models.Model):
    title = models.CharField('Name:', max_length=50)
    category = models.CharField('Category', max_length=50)
    text = models.CharField('Comment to purchase:', max_length=200)
    date = models.DateTimeField('Deadline time/date(example:2024-12-31):')
    image = models.ForeignKey(ProductImage, blank=True, on_delete=models.CASCADE, related_name='images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registration_purchase')
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='registration')
