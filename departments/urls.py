from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.defined, name='departsdefined'),
    url(r'^data/$', views.defineddata, name='departsdefineddata'),
    url(r'^info/$', views.info, name='departsinfo_rel'),
    url(r'^info/(?P<name>.*)/$', views.info, name='departsinfo'),
    url(r'^add/$', views.adddep, name='departsadd'),
    url(r'^edit/$', views.editdep, name='departsedit_rel'),
    url(r'^edit/(?P<name>.*)/$', views.editdep, name='departsedit'),
    url(r'^makedelete/$', views.makedelete, name='departsmakedelete_rel'),
    url(r'^makedelete/(?P<name>.*)/$', views.makedelete, name='departsmakedelete'),
    url(r'^name/$', views.deptname, name='departsname'),
    url(r'^nameother/(?P<name>.*)/$', views.nameother, name='departsnameother'),
    url(r'^shortname/$', views.shortname, name='departsshortname'),
    url(r'^shortnameother/(?P<name>.*)/$', views.shortnameother, name='departsshortnameother'),
    url(r'^infoadmins/(?P<name>.*)/$', views.infoadmins, name='departsinfoadmins'),
    url(r'^infousers/(?P<name>.*)/$', views.infousers, name='departsinfousers'),
    url(r'^addmember/(?P<name>.*)/$', views.addmember, name='departsaddmember'),
    url(r'^deletemember/(?P<name>.*)/(?P<username>.*)/$', views.deletemember, name='departsdeletemember'),
    url(r'^deletemember/(?P<name>.*)/$', views.deletemember, name='departsdeletemember_rel'),
]

