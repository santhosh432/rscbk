from django.db import models
from django.db.models import Q
# Create your models here.
from django.contrib.auth.models import User
from home.models import Brand
# all categories...


class Category(models.Model):
    DEFAULT_PK=1
    category_name = models.CharField(max_length=15, help_text='Category name')
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return '{0}'.format(self.category_name)

class CatBrand(models.Model):
    cat_nam = models.ForeignKey(Category, related_name="cat_name",default=Category.DEFAULT_PK)
    bnd_name = models.ForeignKey(Brand, default=Brand.DEFAULT_PK)

    #def __str__(self):
    #    return '{0}'.format(self.brand_name)

# all items
itemstatus_choice = (
    ('A', 'Available'),
    ('S', 'Sold out'),

)


#class CategoryBrand(models.Model):
#    DEFAULT_PK=1
#    cat_brand_name = models.CharField(max_length=15, help_text='brand name')


class Items(models.Model):
    category = models.ForeignKey(Category)
    bnd = models.ForeignKey(Brand, default=Brand.DEFAULT_PK)
    #cat_bnd = models.ForeignKey(CategoryBrand, default=CategoryBrand.DEFAULT_PK)
    exchange_category = models.ForeignKey(Category, related_name="exchange_category",default=Category.DEFAULT_PK)
    item_name = models.CharField(max_length=25, help_text='item short description')
    item_full_desc = models.CharField(max_length=200, help_text='item full description')
    price = models.PositiveIntegerField(help_text='Item price')
    location = models.CharField(max_length=50, help_text='Item location')
    months_used = models.PositiveSmallIntegerField(help_text='No of Months')
    years_used = models.PositiveSmallIntegerField(help_text='No of Years', default=1)
    itemuser = models.ForeignKey(User, null=True, blank=True)
    item_status = models.CharField(max_length=3, help_text='Current Item Status', choices=itemstatus_choice, default='A')
    item_image = models.ImageField(upload_to='myitems/', help_text='Upload item image 1',default='null')
    item_image2 = models.ImageField(upload_to='myitems/', help_text='Upload item image 2',default='null')
    other_info = models.CharField(max_length=150, help_text="Item other information", default="null")
    def __str__(self):
        return '{0}'.format(self.category, self.item_name)

    def get_absolute_url(self):
        return reverse('edititem', kwargs={'pk': self.pk})




class Wishlist(models.Model):
    wishlist_category = models.ForeignKey(Category)
    wishlist_name = models.CharField(max_length=25, help_text='item short description')
    wishlist_full_desc = models.CharField(max_length=200, help_text='item full description')
    wishlist_user = models.ForeignKey(User, null=True, blank=True)
    wishlist_other_info = models.CharField(max_length=150, help_text="Item other information", default="null")



class Userwhishlist(models.Model):
    item = models.ForeignKey(Items)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        unique_together = (('user', 'item'), )

    def __str__(self):
        return '{0}-{1}'.format(self.item, self.user)