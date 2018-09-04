from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from minerals import views

app_name = 'minerals'
urlpatterns = [
    url(r'^$', views.minerals_list, name="index"),
    url(r'detail/(?P<pk>\d+)/$', views.mineral_detail, name="detail"),
    url(r'search/$', views.search, name='search'),
    url(r'group/(?P<group>[A-Za-z ]+)/$', views.sort_by_group, name='group_sort'),
    url(r'list/(?P<letter>[A-Z])/$', views.sort_by_letter, name='letter_sort'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
