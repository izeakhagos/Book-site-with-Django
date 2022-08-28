from django.contrib import admin
from .models import Category, Book, BookSearch, Comment


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookSearch)
admin.site.register(Comment)



# Register your models here.
