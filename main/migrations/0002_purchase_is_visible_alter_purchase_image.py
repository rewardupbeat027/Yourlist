# Generated by Django 5.0.3 on 2024-04-23 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='is_visible',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='image',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.productimage'),
        ),
    ]