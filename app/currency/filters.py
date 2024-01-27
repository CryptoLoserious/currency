import django_filters

from currency.models import Rate, ContactUs, Source


class RateFilter(django_filters.FilterSet):

    class Meta:
        model = Rate
        fields = {
            'buy': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'sell': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'currency_type': ['exact']
        }


class ContactUsFilter(django_filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = {
            'created': ['date'],
            'subject': ['exact'],
        }


class SourceFilter(django_filters.FilterSet):

    class Meta:
        model = Source
        fields = {
            'name': ['exact'],
            'created': ['date'],
        }
