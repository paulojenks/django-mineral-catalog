from django.conf.urls import url

from minerals import views

app_name = 'minerals'
urlpatterns = [
    url(r'^$', views.minerals_list, name="index"),
    url(r'detail/(?P<pk>\d+)/$', views.mineral_detail, name="detail"),
]