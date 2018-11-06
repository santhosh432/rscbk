"""rscbk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home.views import *
from django.contrib.auth import views as auth_views

from categories import views as catviews

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from categories.cat_api import NoteViewSet

from django.conf.urls import url, include

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)




urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^$', welcome, name='welcome'),
    url(r'^home/$', login, name='login'),
    url(r'^login/$', login, name='login'),
    # url(r'^$',main_home),
    #url(r'^$',auth_views.login, {'template_name': 'home.html'} ,name='login'),
    #url(r'^home/$',auth_views.login, {'template_name': 'home.html'} ,name='login'),
    url(r'^terms/$', terms),
    url(r'^privacy/$', privacy),
    url(r'^wishlist/$', wishlist),
    url(r'^aboutus/$', aboutus),
    url(r'^contactus/$', contactus),
    url(r'^feedback/$', feedback),
    url(r'^dash_help/$', dash_help),
    url(r'^change_password/$', change_password),
    url(r'^signup/$', sign_up),
    #url(r'^login', auth_views.login, {'template_name': 'home.html'} ,name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name="logout"),

    url(r'myuserdashboard/', myuserdashboard ,name='myuserdashboard'),
    url(r'myuserdashboardtest/', myuserdashboardtest ,name='myuserdashboardtest'),

    url(r'^profiles/new/$', NewUserProfileView.as_view(), name="new-user-profile"),
    url(r'^users/(?P<pk>\d+)/edit/$', EditUserProfileView.as_view(), name="edit-user-profile"),

    url(r'addcatbrandlink/(?P<cat_id>\d+)/undefined/undefined$', catviews.addcatbrand ,name='addcatbrandlink'),

    url(r'myuserdashboard_with_cat/(?P<cat_id>\d+)/$', myuserdashboard_with_cat ,name='myuserdashboard_withargument'),
    url(r'myuserdashboard_with_cat_bnd/(?P<cat_id>\d+)/(?P<bnd_id>\d+)/$', myuserdashboard_with_cat_bnd ,name='myuserdashboard_with_cat_bnd'),
    url(r'myuserdashboard_with_cat_bnd/(?P<cat_id>\d+)/(?P<bnd_id>\d+)/(?P<min_id>\d+)/(?P<max_id>\d+)/$', myuserdashboard_with_cat_bnd_min_max ,name='myuserdashboard_with_cat_bnd_min_max'),
    url(r'myuserdashboard_with_cat_freelist/(?P<cat_id>\d+)/$', myuserdashboard_with_cat_freelist ,name='myuserdashboard_with_cat_freelist'),


    url(r'dashboard/',dashboard),
    url(r'additems/',catviews.additems , name='additems'),
    url(r'addwishlist/',catviews.addwishlist , name='addwishlist'),
    url(r'addbrand/',catviews.addbrand , name='addbrand'),
    url(r'addcatbrand/',catviews.addcatbrand , name='addcatbrand'),
    url(r'forget_password/',catviews.forget_password , name='forget_password'),
    url(r'forget_password_reset/',catviews.forget_password_reset , name='forget_password_reset'),

    url(r'view_item/(?P<item_id>\d+)/$',catviews.view_item , name='view_item'),
    url(r'view_item_global/(?P<item_id>\d+)/$',catviews.view_item_global , name='view_item_global'),

    url(r'^edititem/(?P<pk>\d+)$', catviews.edit_item, name="edit_item"),

    url(r'^delete_item/(?P<item_id>\d+)/$',catviews.delete_item, name='delete_item'),
    url(r'^', include('home.urls',namespace="homeapp")),
    url(r'^', include('categories.urls',namespace="categoriesapp")),

    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
