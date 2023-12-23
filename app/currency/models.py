from django.db import models

from currency.choices import CurrencyTypeChoices
from django.utils.translation import gettext_lazy as _


class Rate(models.Model):
    buy = models.DecimalField(_('Buy'), max_digits=10, decimal_places=2)
    sell = models.DecimalField(_('Sell'), max_digits=10, decimal_places=2)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    currency_type = models.IntegerField(
        _('Currency type'),
        choices=CurrencyTypeChoices.choices,
        default=CurrencyTypeChoices.USD
    )
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)  # TODO related_name

    def __str__(self):
        return f'{self.buy} - {self.sell} - {self.source}'


class Source(models.Model):
    source_url = models.CharField(_('URL'), max_length=255)
    name = models.CharField(_('Name'), max_length=64)
    created = models.DateTimeField(_('Created'), auto_now_add=True)

    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    email_from = models.EmailField(_('Email from'), max_length=128)
    subject = models.CharField(_('Subject'), max_length=256)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    body = models.CharField(_('Body'), max_length=2048)

    class Meta:
        verbose_name = _('Contact Us')
        verbose_name_plural = _('Contact Us')


class RequestResponseLog(models.Model):
    path = models.CharField(_('Path'), max_length=128)
    request_method = models.CharField(_('Request'), max_length=8)
    time = models.DecimalField(_('Buy'), max_digits=10, decimal_places=2)
