from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task
import requests

from currency.models import Rate, Source
from currency.choices import CurrencyTypeChoices

from currency.constants import PRIVATBANK_CODE_NAME, MONOBANK_CODE_NAME

from currency.utils import to_2_places_decimal


@shared_task
def parse_privatbank():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
    response = requests.get(url)
    response.raise_for_status()

    source, _ = Source.objects.get_or_create(code_name=PRIVATBANK_CODE_NAME, defaults={'name': 'PrivatBank'})

    rates = response.json()

    available_currency_type = {
        'USD': CurrencyTypeChoices.USD,
        'EUR': CurrencyTypeChoices.EUR
    }

    for rate in rates:
        buy = to_2_places_decimal(rate['buy'])
        sell = to_2_places_decimal(rate['sale'])
        currency_type = rate['ccy']

        if currency_type not in available_currency_type:
            continue

        currency_type = available_currency_type[currency_type]

        last_rate = Rate.objects.filter(source=source, currency_type=currency_type).order_by('-created').first()

        if last_rate is None or last_rate.buy != buy or last_rate.sell != sell:
            Rate.objects.create(
                buy=buy,
                sell=sell,
                currency_type=currency_type,
                source=source
            )


@shared_task
def parse_monobank():
    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()

    source, _ = Source.objects.get_or_create(code_name=MONOBANK_CODE_NAME, defaults={'name': 'MonoBank'})

    rates = response.json()

    available_currency_type = {
        840: CurrencyTypeChoices.USD,
        978: CurrencyTypeChoices.EUR
    }

    for rate in rates:
        buy_key = 'rateBuy'
        sell_key = 'rateSell'
        currency_key = 'currencyCodeA'
        currency_key_2 = 'currencyCodeB'

        if rate.get(currency_key_2) != 980:
            continue

        if buy_key not in rate or sell_key not in rate or currency_key not in rate:
            continue

        buy = to_2_places_decimal(rate[buy_key])
        sell = to_2_places_decimal(rate[sell_key])
        currency_type = rate[currency_key]

        if currency_type not in available_currency_type:
            continue

        currency_type = available_currency_type[currency_type]

        last_rate = Rate.objects.filter(source=source, currency_type=currency_type).order_by('-created').first()

        if last_rate is None or last_rate.buy != buy or last_rate.sell != sell:
            Rate.objects.create(
                buy=buy,
                sell=sell,
                currency_type=currency_type,
                source=source
            )


@shared_task(autoretry_for=(ConnectionError,), retry_kwargs={
    'max_retries': 5
})
def send_email_in_background(subject, body):
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )
