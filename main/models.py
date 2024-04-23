from django.db import models


# Create your models here.

class Purchase(models.Model):
    title = models.CharField('Name:', max_length=50)
    category = models.CharField('Category', max_length=50)
    text = models.CharField('Comment to purchase:', max_length=200)
    date = models.DateTimeField('Deadline time/date(example:2024-12-31):')
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

