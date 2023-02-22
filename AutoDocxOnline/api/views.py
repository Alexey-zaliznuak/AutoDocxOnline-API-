from documents.models import Document
from django.http import FileResponse

from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .serializers import DocumentSerializer, DocumentsPackageSerializer
from .permissions import IsOwnerOrReadOnlyPermission, IsOwnerOrObjIsPublic

from documents.models import Document, DocumentsPackage


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = (IsOwnerOrReadOnlyPermission,)

    def get_queryset(self):
        # protect “AnonymousUser” is not a valid UUID
        if not self.request.user.is_anonymous:
            new_queryset = Document.objects.filter(owner=self.request.user)
            return new_queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DocumentsPackageViewSet(viewsets.ModelViewSet):
    queryset = DocumentsPackage.objects.all()
    serializer_class = DocumentsPackageSerializer
    permission_classes = (IsOwnerOrReadOnlyPermission,)

    def get_queryset(self):
        # protect “AnonymousUser” is not a valid UUID
        if not self.request.user.is_anonymous:
            new_queryset = DocumentsPackage.objects.filter(owner=self.request.user)
            return new_queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


def upload(request, document_id):
    document = Document.objects.get(pk=document_id)
    if not document.public:
        if request.user != document.owner:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    response = FileResponse(open(document.file.path, 'rb'))

    return response
