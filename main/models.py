from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Purchase(models.Model):
    title = models.CharField('Name:', max_length=50)
    category = models.CharField('Category', max_length=50)
    text = models.CharField('Comment to purchase:', max_length=200)
    date = models.DateTimeField('Deadline time/date(example:2012-03-13 21:12:20):')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registration_purchase')
    is_visible = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title


class Registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='registration')
