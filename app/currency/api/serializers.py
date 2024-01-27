from rest_framework import serializers
from django.core.mail import send_mail

from currency.models import Rate, ContactUs, Source


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sell',
            'created',
            'source',
            'currency_type',
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_from',
            'subject',
            'body',
        )

    def create(self, validated_data):
        contact_us_instance = ContactUs.objects.create(**validated_data)

        send_mail(
            validated_data['subject'],
            validated_data['body'],
            validated_data['email_from'],
            ['wisp777test@gmail.com'],
            fail_silently=False,
        )

        return contact_us_instance


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'source_url',
            'name',
            'logo',
        )
