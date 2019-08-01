from django.db import models

# Create your models here.
from datetime import date
import datetime
from django.contrib.auth.models import User

# Create your models here.
PRIORITY = (
        ('HIGH', 'HIGH'),
        ('MEDIUM', 'MEDIUM'),
        ('LOW', 'LOW'),
    )
MONTH = (
        ('1', 'JAN'),
        ('2', 'FEB'),
        ('3', 'MAR'),
        ('4', 'APR'),
        ('5', 'MAY'),
        ('6', 'JUN'),
        ('7', 'JUL'),
        ('8', 'AUG'),
        ('9', 'SEPT'),
        ('10', 'OCT'),
        ('11', 'NOV'),
        ('12', 'DEC'),
    )

STATUS = (
        ('NOTSTARTED', 'NOT-STARTED'),
        ('INPROGRESS', 'IN-PROGRESS'),
        ('FIXED', 'FIXED'),
    )
STATUS1 = (
        ('WEBSITE', 'WEBSITE'),
        ('MOBILEAPP', 'MOBILEAPP'),
        ('BUSINESS', 'BUSINESS'),
    )
class Bugs(models.Model):
    bug_title = models.CharField(max_length=80,blank=True, null=True)
    bug_detail = models.CharField(max_length=200,blank=True, null=True)
    priority = models.CharField(max_length=10, blank=True, null=True, choices=PRIORITY)
    status = models.CharField(max_length=100, blank=True, null=True, choices=STATUS)
    remark= models.CharField(max_length=100 ,blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True, choices=STATUS1)
    reported_by = models.ForeignKey(User,related_name = "reported_by", blank=True, null=True, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, blank=True,null=True, related_name = "assigned_to", on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/',default = 'bugissue/default/no-img.jpg')
