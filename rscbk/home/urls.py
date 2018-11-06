from django.conf.urls import include, url

from home import views


urlpatterns =[
    url(r'^udb_home/$', views.udb_home, name="udb_home"), # this is user dashboard
    url(r'^udb_aboutus/$', views.udb_aboutus, name="udb_aboutus"), # this is site aboutus
    url(r'^udb_help/$', views.udb_help, name="udb_help"), # this is for help
    url(r'^udb_notifications/$', views.udb_notifications, name="udb_notifications"), # this is for notifications
    url(r'^udb_whishlist/$', views.udb_whishlist, name="udb_whishlist"), # this is for notifications
    url(r'^udb_righthome/$', views.udb_righthome, name="udb_righthome"), # this is for notifications
    url(r'^udb_addmyitems/$', views.udb_addmyitems, name="udb_addmyitems"), # this is for notifications
    url(r'^udb_myprofile/$', views.udb_myprofile, name="udb_myprofile"), # this is for notifications
    url(r'^udb_change_pwd/$', views.udb_change_pwd, name="udb_change_pwd"), # this is for notifications

    url(r'^ajax/del_item/$', views.del_item, name="del_item"), # this is for notifications
    url(r'^ajax/addtowishlist/$', views.udb_addtowishlist, name="udb_addtowishlist"),  # this is cat details
    url(r'^ajax/addto_vieweditem/$', views.udb_addto_vieweditem, name="udb_addto_vieweditem"),  # the item will add when user is viewed

]
