# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse, HttpResponseRedirect
# Register your models here.
from .models import Brand,UserFullProfile,Feedback


@admin.register(UserFullProfile)
class UserFullProfileAdmin(admin.ModelAdmin):
    list_display = ['mobile','user']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand_name']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display =['customer_name', 'comment']

class CustomUserAdmin(UserAdmin):
    actions = ['send_mail_to_users','email_one']
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_superuser', 'id','last_login']
    ordering = ['id']
    def send_mail_to_users(modeladmin, request, qs):
        subject = "Reminder to upload the Items in the portal Barterkings.in ."
        from_mail = 'barterkingsindia@gmail.com'

        for sm in qs:
            msg = mark_safe("""Hi {0}, \n We have observed that you have not uploaded or few items uploads in the Barterkings.in Portal.\n \n
            Please share/upload your Items which you want to exchange or sell in the portal so that we can use the maximum functionality of the website.\n
            Thanks and Regards, \n Barterkings Admin \n * This is an Auto Generated Message Please donot reply to this mail.  """.format(sm.username) )

            msg_plain = render_to_string('email.txt', {'user': sm.username})
            send_mail(subject, msg_plain, from_mail,[sm.email], fail_silently=False, )
        messages.info(request, 'Email sent successfully...')

    def email_one(modeladmin, request, qs):
        subject = "Reminder to upload the Items in the portal Barterkings.in ."
        from_email = 'barterkingsindia@gmail.com'

        for smuser in qs:
            ctx = {'user':smuser.username}

            message = render_to_string('email.txt', ctx)

            EmailMessage(subject, message, to=[smuser.email], from_email=from_email).send()

            return HttpResponse('email_one')
        messages.info(request, 'new Email sent successfully...')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
