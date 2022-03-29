from django.contrib import admin

from blog.models import Author, Post, Tag

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tag", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
