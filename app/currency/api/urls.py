from django.urls import path
from rest_framework import routers

from currency.api.views import (RateViewSet,
                                ContactUsViewSet,
                                SourceListAPIView)


router = routers.SimpleRouter(trailing_slash=True)
router.register(r'rates', RateViewSet, basename='rate')
router.register(r'contactuses', ContactUsViewSet, basename='contactus')
# router.register(r'sources', SourceViewSet, basename='source')


app_name = 'currency_api'

urlpatterns = [
    # path('rates/', RateListAPIView.as_view(), name='rate-list'),
    # path('contactus/', ContactUsListAPIView.as_view(), name='contactus-list'),
    path('sources/', SourceListAPIView.as_view(), name='source-list'),
    #
    # path('rates/<int:pk>/', RateDetailsAPIView.as_view(), name='rate-details'),
    # path('contactus/<int:pk>/', ContactUsDetailsAPIView.as_view(), name='contactus-details'),
] + router.urls
