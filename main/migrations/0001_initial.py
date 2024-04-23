# Generated by Django 5.0.3 on 2024-03-20 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Name:')),
                ('image', models.ImageField(upload_to='')),
                ('category', models.CharField(max_length=50, verbose_name='Category')),
                ('text', models.CharField(max_length=200, verbose_name='Comment to purchase:')),
                ('date', models.DateTimeField(verbose_name='Deadline time/date:')),
            ],
        ),
    ]
