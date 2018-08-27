from django.conf.urls import include, url

from categories import views


urlpatterns =[
    url(r'^udb_add_item/$', views.udb_add_item, name="udb_add_item"), # this is user add item
    url(r'^cat_details/$', views.cat_details, name="cat_details"), # this is cat details

    ]
