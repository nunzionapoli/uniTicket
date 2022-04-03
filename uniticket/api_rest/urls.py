from django.urls import path, re_path
from rest_framework import routers
from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework.schemas import get_schema_view

from api_rest.views import (
  GroupViewSet, TicketAPIDetail,
  TicketAPIStruttureList,
  TicketAPITicketCategoryList, TicketAPIView,
  UserViewSet
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)


urlpatterns = [
  # path('api/', include(router.urls)),
  # path('api-auth/', include(rest_framework.urls, 'rest_framework',)),

  re_path(
    '^openapi$',
    get_schema_view(**{}),
    name='openapi-schema'
  ),
  re_path(
    '^openapi.json$',
    get_schema_view(
      renderer_classes = [JSONOpenAPIRenderer], **{}
    ),
    name='openapi-schema-json'
  ),

  path(
    'api/<slug:structure_slug>/<slug:category_slug>/ticket/new',
    TicketAPIView.as_view(),
    name='api-new-ticket'
  ),

  path(
    'api/ticket/<str:ticket_uid>',
    TicketAPIDetail.as_view(),
    name='api-view-ticket'
  ),

  path(
    'api/strutture/list',
    TicketAPIStruttureList.as_view(),
    name='api-strutture-list'
  ),

  path(
    'api/ticket/category/list',
    TicketAPITicketCategoryList.as_view(),
    name='api-ticket-category-list'
  ),


]
