from django.shortcuts import render
from django.http.response import HttpResponse
from currency.models import Rate, ContactUs
def rate_list(request):

    results = []
    rates = Rate.objects.all()

    for rate in rates:
        results.append(
            f'ID: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, type: {rate.type}, source: {rate.source},'
            f'created: {rate.created} <br>'
        )
    return HttpResponse(str(results))

def message_list(request):

    results2 = []
    contacts = ContactUs.objects.all()

    for contact in contacts:
        results2.append(
            f'email: {contact.email_from}, subject: {contact.subject}, message: {contact.message} <br>'
        )
    return HttpResponse(str(results2))