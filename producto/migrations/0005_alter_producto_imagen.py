# Generated by Django 4.2.5 on 2023-10-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
