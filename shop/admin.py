from django.contrib import admin
from .models import Category, Product, Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug']
    list_editable = ['description']
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'category', 'description']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'item', 'rating', 'timestamp']
    list_editable = ['text']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin,)
admin.site.register(Review, ReviewAdmin)
