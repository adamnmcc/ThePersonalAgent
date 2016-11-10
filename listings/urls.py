from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sales', views.sales, name='sales'),
    url(r'^exchanged', views.exchanged, name='exchanged'),
    url(r'^fallen_through', views.fallen_through, name='fallen_Through'),
    url(r'^new', views.listing_new, name='listing_new'),

]
