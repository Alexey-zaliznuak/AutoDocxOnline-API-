from django.contrib import admin
from .models import Document, DocumentsPackage, User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm


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
        'pk',
        'name',
        'file',
        'owner',
    )
    search_fields = ('name', 'file')
    list_filter = ('name',)
    empty_value_display = '-пусто-'
