# Generated by Django 3.2.7 on 2021-10-28 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comaterialesApp', '0005_auto_20211018_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='descargas/'),
        ),
    ]
