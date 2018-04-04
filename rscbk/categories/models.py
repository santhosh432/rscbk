from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# all categories...
class Category(models.Model):
    DEFAULT_PK=1
    category_name = models.CharField(max_length=15, help_text='Category name')
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return '{0}'.format(self.category_name)


# all items
itemstatus_choice = (
    ('A', 'Available'),
    ('S', 'Sold out'),

)


class Items(models.Model):
    category = models.ForeignKey(Category)
    exchange_category = models.ForeignKey(Category, related_name="exchange_category",default=Category.DEFAULT_PK)
    item_name = models.CharField(max_length=25, help_text='item short description')
    item_full_desc = models.CharField(max_length=200, help_text='item full description')
    price = models.PositiveIntegerField(help_text='Item price')
    location = models.CharField(max_length=50, help_text='Item location')
    months_used = models.PositiveSmallIntegerField(help_text='No of Years')
    years_used = models.PositiveSmallIntegerField(help_text='No of Months')
    itemuser = models.ForeignKey(User, null=True, blank=True)
    item_status = models.CharField(max_length=3, help_text='Current Item Status', choices=itemstatus_choice, default='A')
    item_image = models.ImageField(upload_to='myitems/', help_text='Upload item image 1',default='null')
    item_image2 = models.ImageField(upload_to='myitems/', help_text='Upload item image 2',default='null')
    def __str__(self):
        return '{0}'.format(self.category, self.item_name)
