# from django.shortcuts import render
# from django.http.response import HttpResponse
from django.shortcuts import render
from currency.models import Rate, ContactUs


def rate_list(request):

    rates = Rate.objects.all()
    context = {
        'rates': rates
    }

    return render(request, 'rate_list.html', context)


def message_list(request):

    contacts = ContactUs.objects.all()
    context2 = {
        'contacts': contacts
    }

    return render(request, 'contactUs.html', context2)
