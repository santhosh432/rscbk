from django.db import models

# Create your models here.


# all categories...
class Category(models.Model):
    category_name = models.CharField(max_length=15, help_text='Category name')
    status = models.BooleanField(default=False)

    def __str__(self):
        return '{0}'.format(self.category_name)


# all items
class Items(models.Model):
    category = models.ForeignKey(Category)
    item_name = models.CharField(max_length=25, help_text='item short description')
    item_full_desc = models.CharField(max_length=200, help_text='item full description')
    price = models.PositiveIntegerField(help_text='Item price')
    location = models.CharField(max_length=50, help_text='Item location')
    months_used = models.PositiveSmallIntegerField(help_text='No of Years')
    years_used = models.PositiveSmallIntegerField(help_text='No of Months')

    def __str__(self):
        return '{0}'.format(self.category, self.item_name)
