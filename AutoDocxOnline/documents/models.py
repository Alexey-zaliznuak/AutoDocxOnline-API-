import uuid
from django.db import models
from utils import user_documents_directory_path
from django.contrib.auth.models import AbstractUser, User


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class PublicModel(models.Model):
    #This field use in IsOwnerOrObjIsPublic permission
    public = models.BooleanField(verbose_name="is public", default=False)

    class Meta:
        abstract = True


class Document(PublicModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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


class DocumentsPackage(PublicModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
