from django.conf.urls import include, url

from home import views


urlpatterns =[
    url(r'^udb_home/$', views.udb_home, name="udb_home"), # this is user dashboard
    url(r'^udb_aboutus/$', views.udb_aboutus, name="udb_aboutus"), # this is site aboutus
    url(r'^udb_help/$', views.udb_help, name="udb_help"), # this is for help
    url(r'^udb_notifications/$', views.udb_notifications, name="udb_notifications"), # this is for notifications
    url(r'^udb_whishlist/$', views.udb_whishlist, name="udb_whishlist"), # this is for notifications
    url(r'^udb_righthome/$', views.udb_righthome, name="udb_righthome"), # this is for notifications

    ]
