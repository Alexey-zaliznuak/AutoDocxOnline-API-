# Generated by Django 3.2 on 2023-02-13 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='file_name')),
                ('file', models.FileField(upload_to='documents/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL, verbose_name='document_author')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DocumentsPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='package_name')),
                ('documents', models.ManyToManyField(to='documents.Document', verbose_name='documents')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents_packages', to=settings.AUTH_USER_MODEL, verbose_name='documents_package_author')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
