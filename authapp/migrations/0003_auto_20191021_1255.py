# Generated by Django 2.2.6 on 2019-10-21 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20191020_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='reg',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('uname', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
                ('cpwd', models.CharField(max_length=20)),
                ('mobno', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='regmodel',
        ),
    ]
