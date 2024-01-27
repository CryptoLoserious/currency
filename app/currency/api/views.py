from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework import filters
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework.generics import ListCreateAPIView
from currency.api.paginators import RatePagination, ContactUsPagination, SourcePagination
from currency.api.serializers import RateSerializer, ContactUsSerializer, SourceSerializer
from currency.api.throtling import RateThrottle
from currency.models import Rate, ContactUs, Source


# class RateListAPIView(ListCreateAPIView):
#     queryset = Rate.objects.all().order_by('-created')
#     serializer_class = RateSerializer  # json -> obj, obj -> json
#     renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
#
#
# class ContactUsListAPIView(ListAPIView):
#     queryset = ContactUs.objects.all().order_by('-created')
#     serializer_class = ContactUsSerializer  # json -> obj, obj -> json
#     renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)


class SourceListAPIView(ListCreateAPIView):
    queryset = Source.objects.all().order_by('-created')
    serializer_class = SourceSerializer  # json -> obj, obj -> json
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = SourcePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['source_url', 'name']


# class RateDetailsAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all().order_by('-created')
#     serializer_class = RateSerializer
# #     renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
#
#
# class ContactUsDetailsAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = ContactUs.objects.all().order_by('-created')
#     serializer_class = ContactUsSerializer  # json -> obj, obj -> json


class RateViewSet(ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer  # json -> obj, obj -> json
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = RatePagination
    # filterset_class = RateFilter
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'buy', 'sell', 'created', 'source__name']
    throttle_classes = (RateThrottle,)


class ContactUsViewSet(ModelViewSet):
    queryset = ContactUs.objects.all().order_by('-created')
    serializer_class = ContactUsSerializer  # json -> obj, obj -> json
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)

    pagination_class = ContactUsPagination
    # filterset_class = ContactUsFilter
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'email_from', 'subject']


# class SourceViewSet(ModelViewSet):
#     queryset = Source.objects.all().order_by('-created')
#     serializer_class = SourceSerializer  # json -> obj, obj -> json
#     renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
#
#
# #     pagination_class = RatePagination
# #     filterset_class = RateFilter
# #     filter_backends = (
# #         DjangoFilterBackend,
# #         OrderingFilter,
# #     )
# #     ordering_fields = ('buy', 'sell', 'created')
# #     throttle_classes = (RateThrottle,)
