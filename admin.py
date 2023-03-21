from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'text', 'url')
    list_filter = ('name',)
    search_fields = ('name', 'text', 'url')
    ordering = ('name', 'parent__id', 'text')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parent':
            kwargs['queryset'] = MenuItem.objects.filter(name=request.resolver_match.kwargs['menu_name'])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

