# Generated by Django 2.2.7 on 2019-12-01 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191130_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='coreo',
            new_name='correo',
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.CharField(max_length=255, verbose_name='Imagen'),
        ),
    ]