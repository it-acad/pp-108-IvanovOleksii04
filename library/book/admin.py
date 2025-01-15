from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'authors_list', 'count')
    search_fields = ('name', 'authors__name')
    list_filter = ('authors',)  # Видалено 'publication_year', якщо його немає
    ordering = ('name',)

    fieldsets = (
        ('Book Details', {
            'fields': ('name', 'description', 'count', 'authors')  # Видалено 'publication_year', якщо його немає
        }),
    )

    def authors_list(self, obj):
        """Return a comma-separated list of authors for the book."""
        return ', '.join([author.name for author in obj.authors.all()])
    authors_list.short_description = 'Authors'
