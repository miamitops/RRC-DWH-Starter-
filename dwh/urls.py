# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dwh_data.data_views.default import DefaultView
import dwh_data.urls 
from userena import views as userena_views
from rest_framework import routers
from accounts import views as apiviews

router = routers.DefaultRouter()
router.register(r'users', apiviews.UserViewSet)
router.register(r'groups', apiviews.GroupViewSet)

admin.autodiscover()
from dwh_data.views import PageView, DWHImport
pageView = PageView()
importer = DWHImport()
urlpatterns = i18n_patterns('',
    url(r'^$', pageView.index),
    url(r'^country/(?P<countryid>(?!(sitrep)/)[\@\.\w-]+)/$',  pageView.countrySitRep,  name='country_sitrep'),
    url(r'^situation/(?P<situationid>(?!(sitrep)/)[\@\.\w-]+)/$',  pageView.situationSitRep,  name='situation_report'),
    url(r'^accounts/login/', userena_views.signin, name='userena_signin'),
    url(r'^accounts/logout/', pageView.logout),
    url(r'^stats/insert/(?P<countryid>[\@\.\w-]+)/$', pageView.saveCountryStat),
    url(r'^stats/import/csv/ken', importer.importfiles),
    url(r'^accounts/(?P<username>(?!(signout|signup|signin)/)[\@\.\w-]+)/$',  userena_views.profile_detail,  name='userena_profile_detail'), 
    url(r'^accounts/(?P<username>[\@\.\w-]+)/edit/$',  userena_views.profile_edit, name='userena_profile_edit'),
    url(r'^report_builder/', include('report_builder.urls')),
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^c/', include(dwh_data.urls)),
    url(r'^about/', DefaultView.as_view()),    
    url(r'^accounts/', include('accounts.urls')),
     
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
