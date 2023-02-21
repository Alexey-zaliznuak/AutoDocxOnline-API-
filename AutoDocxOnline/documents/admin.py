from django.contrib import admin
from .models import Document, DocumentsPackage, User

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'file',
        'owner',
    )
    search_fields = ('name', 'file')
    list_filter = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(User)
