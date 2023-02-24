from django.contrib import admin
from django.urls import reverse
from .models import Document, DocumentsPackage, User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.http import request


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


@admin.register(User)
class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ()}),
    )


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'public',
        'owner',
        'file_path',
        'pk',
    )
    search_fields = ('name', 'owner__username',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'

    @admin.display(empty_value='unknown', description="download_url")
    def file_path(self, obj):
        return reverse(
            'documents-download_document',
                args=(
                obj.pk,
            )
        )
