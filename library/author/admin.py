from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Видалено 'birth_date' і 'country', якщо їх немає
    search_fields = ('name',)
    list_filter = ()  # Видалено 'birth_date' і 'country', якщо їх немає
    ordering = ('name',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('name',)  # Залишено тільки існуючі поля
        }),
    )
