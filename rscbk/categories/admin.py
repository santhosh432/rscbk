from django.contrib import admin
from import_export import resources # dj import -export
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import * #,CategoryBrand


#@admin.register(CategoryBrand)
#class CategoryBrandAdmin(admin.ModelAdmin):
#    pass#list_display = ['category_name','status']


@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
   list_display = ['itemuser','id','category','item_name', 'price', 'location',]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','status']

class BrandResource(resources.ModelResource):
    class Meta:
        model = CatBrand
        exclude = ('id',)
        fields = ('cat_nam','bnd_name',)
        import_id_fields = ('cat_nam','bnd_name',)


@admin.register(CatBrand)
class CatBrandAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['cat_nam','bnd_name']


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['wishlist_category','wishlist_name','wishlist_full_desc','wishlist_user','wishlist_other_info']

Wishlist
#CatBrand