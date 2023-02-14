from rest_framework import serializers


def file_is_docx(value:str):
    if not value.endswith('.docx'):
        raise serializers.ValidationError("file must be 'docx' document")
