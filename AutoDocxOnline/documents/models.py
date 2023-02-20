from django.db import models
from django.contrib.auth import get_user_model
from utils import user_documents_directory_path

User = get_user_model()


class Document(models.Model):
    name = models.CharField(max_length=100, verbose_name='file_title')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='documents',
        verbose_name="document_author",
    )
    file = models.FileField(upload_to=user_documents_directory_path)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return str(self.file.name)


class DocumentsPackage(models.Model):
    name = models.CharField(max_length=100, verbose_name='package_name')
    documents = models.ManyToManyField(Document, verbose_name="documents")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='documents_packages',
        verbose_name="documents_package_author",
    )

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
