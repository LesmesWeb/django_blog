# Generated by Django 2.2.7 on 2019-12-16 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191130_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='correo',
            field=models.EmailField(max_length=254, verbose_name='Correo electronico'),
        ),
    ]