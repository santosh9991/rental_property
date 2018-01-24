from django.conf.urls import url
from homely import views
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # url(r'^$', views.property_details),
    url(r'^$', views.PropertyDetailsList.as_view()),
    url(r'^users_list$', views.UserDetails.as_view()),
    url(r'^owners_list$', views.OwnerDetails.as_view()),
    url(r'^owners_list/(?P<pk>[0-9]+)$', views.OwnerDetails.as_view()),
    url(r'^properties_list$', views.PropertyDetailsList.as_view()),
    url(r'^properties_list/(?P<pk>[0-9]+)$', views.PropertyDetailsList.as_view()),
    url(r'^owner_property$', views.OwnerPropertyDetailsList.as_view()),
    url(r'^owner_property/(?P<owner_id>[0-9]+)$', views.UDOwnerPropertyDetailList.as_view()),
    url(r'^(?P<pk>[0-9]+)$', views.PropertyDetail.as_view()),
]