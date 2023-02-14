from rest_framework import serializers
from documents.models import Document, DocumentsPackage
from .fields import Base64FileField
from .validators import file_is_docx


class DocumentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        pk_field=serializers.CharField(),
        source='owner.username',
        read_only=True
    )
    file = Base64FileField()

    class Meta:
        fields = '__all__'
        model = Document
        read_only_fields = ('owner',)


class DocumentsPackageSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        pk_field=serializers.CharField(),
        source='owner.username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = DocumentsPackage
        read_only_fields = ('owner',)
