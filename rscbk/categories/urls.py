from django.conf.urls import include, url

from categories import views


urlpatterns =[
    url(r'^udb_add_item/$', views.udb_add_item, name="udb_add_item"), # this is user add item
    url(r'^udb_cat_details/(?P<pk>\d+)$', views.udb_cat_details, name="udb_cat_details"), # this is cat details
    url(r'^udb_full_item_details/(?P<pk>\d+)$', views.udb_full_item_details, name="udb_full_item_details"), # this is cat details
    url(r'^udb_lefthome/$', views.udb_lefthome, name="udb_lefthome"),  # this is for notifications

]
