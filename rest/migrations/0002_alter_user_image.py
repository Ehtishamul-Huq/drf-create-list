# Generated by Django 3.2 on 2021-04-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, unique=True, upload_to=''),
        ),
    ]
