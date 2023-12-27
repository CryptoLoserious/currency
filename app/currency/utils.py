from decimal import Decimal, ROUND_DOWN
# from currency.choices import CurrencyTypeChoices
# from currency.models import Rate, Source


def to_2_places_decimal(value: str) -> Decimal:
    return Decimal(value).quantize(Decimal('0.00'), rounding=ROUND_DOWN)


# def compare_currencies(source, rates):
#     for rate in rates:
#         buy = to_2_places_decimal(rate['rateBuy'])
#         sell = to_2_places_decimal(rate['rateSell'])
#         currency_code = rate['currencyCodeA']
#
#         if currency_code == 840:
#             currency_type = CurrencyTypeChoices.USD
#         elif currency_code == 978:
#             currency_type = CurrencyTypeChoices.EUR
#         else:
#             continue
#
#     last_rate = Rate.objects.filter(source=source, currency_type=currency_type).order_by('-created').first()
#
#     if last_rate is None or last_rate.buy != buy or last_rate.sell != sell:
#         Rate.objects.create(
#             buy=buy,
#             sell=sell,
#             currency_type=currency_type,
#             source=source
#         )
