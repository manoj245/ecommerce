# Generated by Django 2.2.6 on 2019-11-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
