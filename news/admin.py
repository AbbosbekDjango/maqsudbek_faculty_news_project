from django.contrib import admin
from .models import News, Category,Contact

# Register your models here.

# admin.site.register(News)
# admin.site.register(Category)
@admin.register(News)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', "slug", "category", "published_time", "status"]
    list_filter = ["status", "created_time", "published_time"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["status", "published_time"]
    date_hierarchy = "published_time"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    search_fields = ['email']