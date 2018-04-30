from django.contrib import admin

# Register your models here.
from .models import Category,Items,CatBrand#,CategoryBrand


#@admin.register(CategoryBrand)
#class CategoryBrandAdmin(admin.ModelAdmin):
#    pass#list_display = ['category_name','status']


@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
   list_display = ['category','item_name', 'price', 'location',]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','status']

@admin.register(CatBrand)
class CatBrandAdmin(admin.ModelAdmin):
    list_display = ['cat_nam','bnd_name']
#CatBrand