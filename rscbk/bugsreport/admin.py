from django.contrib import admin


from bugsreport.models import *



from django import forms



class BugsAdmin(admin.ModelAdmin):
    list_display = ('bug_title', 'assigned_to', 'priority', 'status', 'remark')
    list_filter = ('category','priority','status')
    search_fields = ('bug_title', 'bug_detail', 'priority', 'status',)
    #date_hierarchy = 'created_on'

admin.site.register(Bugs, BugsAdmin)





