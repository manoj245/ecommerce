# Generated by Django 2.2.6 on 2019-11-14 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0005_auto_20191114_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='photo',
        ),
        migrations.AddField(
            model_name='cart',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
