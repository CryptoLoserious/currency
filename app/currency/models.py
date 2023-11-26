from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sell = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField()
    currency_type = models.CharField(max_length=4)
    source = models.CharField(max_length=255)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=30)
    subject = models.CharField(max_length=255)
    message = models.TextField()
