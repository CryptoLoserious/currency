from unittest.mock import MagicMock

from currency.choices import CurrencyTypeChoices
from currency.constants import PRIVATBANK_CODE_NAME, MONOBANK_CODE_NAME
from currency.models import Rate, Source
from currency.tasks import parse_privatbank, parse_monobank


def test_parse_privatbank(mocker):
    initial_count = Rate.objects.count()

    privatbank_data = [
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "40.80000", "sale": "41.80000"},
        {"ccy": "USD", "base_ccy": "UAH", "buy": "37.50000", "sale": "38.10000"},
        {"ccy": "PLN", "base_ccy": "UAH", "buy": "37.50000", "sale": "38.10000"}
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: privatbank_data)
    )

    parse_privatbank()

    assert Rate.objects.count() == initial_count + 2
    assert requests_get_mock.call_count == 1
    assert requests_get_mock.call_args[0][0] == 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'


def test_parse_privatbank_prevent_duplicates(mocker):

    privatbank_data = [
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "40.80000", "sale": "41.80000"},
        {"ccy": "USD", "base_ccy": "UAH", "buy": "37.50000", "sale": "38.10000"},
        {"ccy": "PLN", "base_ccy": "UAH", "buy": "37.50000", "sale": "38.10000"},
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: privatbank_data)
    )

    source, _ = Source.objects.get_or_create(code_name=PRIVATBANK_CODE_NAME, defaults={'name': 'PrivatBank'})
    Rate.objects.create(source=source, buy="40.80", sell="41.80", currency_type=CurrencyTypeChoices.EUR)
    Rate.objects.create(source=source, buy="37.50", sell="38.10", currency_type=CurrencyTypeChoices.USD)
    initial_count = Rate.objects.count()

    parse_privatbank()

    assert Rate.objects.count() == initial_count
    assert requests_get_mock.call_count == 1


def test_parse_monobank(mocker):
    initial_count = Rate.objects.count()

    monobank_data = [
        {"currencyCodeA": 840, "currencyCodeB": 980, "rateBuy": 37.47, "rateSell": 38.00},
        {"currencyCodeA": 978, "currencyCodeB": 980, "rateBuy": 40.45, "rateSell": 41.22},
        {"currencyCodeA": 958, "currencyCodeB": 970, "rateBuy": 41.45, "rateSell": 40.22},
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: monobank_data)
    )

    parse_monobank()

    assert Rate.objects.count() == initial_count + 2
    assert requests_get_mock.call_count == 1
    assert requests_get_mock.call_args[0][0] == 'https://api.monobank.ua/bank/currency'


def test_parse_monobank_prevent_duplicates(mocker):

    monobank_data = [
        {"currencyCodeA": 840, "currencyCodeB": 980, "rateBuy": 37.46, "rateSell": 38.00},
        {"currencyCodeA": 978, "currencyCodeB": 980, "rateBuy": 35.00, "rateSell": 36.00},
        {"currencyCodeA": 958, "currencyCodeB": 970, "rateBuy": 41.45, "rateSell": 40.22}
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: monobank_data)
    )

    source = Source.objects.get(code_name=MONOBANK_CODE_NAME)
    Rate.objects.create(source=source, buy="37.46", sell="38.00", currency_type=CurrencyTypeChoices.USD)
    Rate.objects.create(source=source, buy="35.00", sell="36.00", currency_type=CurrencyTypeChoices.EUR)

    initial_count = Rate.objects.count()
    parse_monobank()

    assert Rate.objects.count() == initial_count
    assert requests_get_mock.call_count == 1
