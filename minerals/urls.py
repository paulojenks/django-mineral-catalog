from django.conf.urls import url

from minerals import views

app_name = 'minerals'
urlpatterns = [
    url(r'^$', views.minerals_list, name="index"),
    url(r'detail/(?P<pk>\d+)/$', views.mineral_detail, name="detail"),
    url(r'search/$', views.search, name='search'),
    url(r'list/(?P<letter>[A-Z])/$', views.sort_by_letter, name='letter_sort'),
    url(r'group/(?P<group>\w+)/$', views.sort_by_group, name='group_sort'),
]