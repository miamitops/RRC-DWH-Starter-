from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.DWHDataList.as_view(), name='DWHData_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.DWHDataDetail.as_view(), name='DWHData_detail'),
    url(r'^create/$', views.DWHDataCreate.as_view(), name='DWHData_create'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.DWHDataUpdate.as_view(), name='DWHData_edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        views.DWHDataDelete.as_view(),
        name='DWHData_delete'),
]