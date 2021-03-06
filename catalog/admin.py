from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter=('status', 'due_back')

    fieldsets = (
        ("Information", {
            'fields':('book', 'imprint', 'id')
        }),
        ('Available', {
            'fields':('status', 'due_back')
        }),
    )

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'date_of_birth', 'date_of_death')

    fields =['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


class BookInstanceInline(admin.TabularInline):
    model = models.BookInstance


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'display_genre')
    inlines=[BookInstanceInline]