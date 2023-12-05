from django.db import models


class CurrencyTypeChoices(models.IntegerChoices):
    USD = 1, 'Dollar'
    EUR = 2, 'Euro'
    BTC = 3, 'Bitcoin'
    ETH = 4, 'Ethereum'
