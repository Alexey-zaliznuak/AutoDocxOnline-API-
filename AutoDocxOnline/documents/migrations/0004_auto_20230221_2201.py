# Generated by Django 3.2 on 2023-02-21 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_documentspackage_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='public',
            field=models.BooleanField(default=False, verbose_name='is public'),
        ),
        migrations.AlterField(
            model_name='documentspackage',
            name='public',
            field=models.BooleanField(default=False, verbose_name='is public'),
        ),
    ]