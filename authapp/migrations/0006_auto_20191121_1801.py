# Generated by Django 2.2.6 on 2019-11-21 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20191022_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='uname',
            new_name='username',
        ),
    ]
