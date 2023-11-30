from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sell = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    currency_type = models.CharField(max_length=4)


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=30)
    subject = models.CharField(max_length=255)
    message = models.TextField()
