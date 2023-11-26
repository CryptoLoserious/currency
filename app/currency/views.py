# from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm, ContactUsForm
from django.views.decorators.csrf import csrf_exempt


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


def source_list(request):

    source = Source.objects.all()
    context3 = {
        'source': source
    }

    return render(request, 'source_list.html', context3)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(data=request.POST)
        # print(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')

    else:
        form = SourceForm()

    context3 = {
        'form': form
    }

    return render(request, 'source_create.html', context3)


def contactUs_create(request):
    if request.method == 'POST':
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/message/list/')

    else:
        form = ContactUsForm()

    context2 = {
        'form': form
    }

    return render(request, 'contactUs_create.html', context2)


def rate_create(request):
    if request.method == 'POST':
        form = RateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')

    else:
        form = RateForm()

    context = {
        'form': form
    }

    return render(request, 'rate_create.html', context)


def rate_update(request, pk):
    rate = get_object_or_404(Rate, id=pk)

    if request.method == 'POST':
        form = RateForm(data=request.POST, instance=rate)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')

    elif request.method == 'GET':
        form = RateForm(instance=rate)

    context = {
        'form': form
    }

    return render(request, 'rate_update.html', context)


def contactUs_update(request, pk):
    contacts = get_object_or_404(ContactUs, id=pk)

    if request.method == 'POST':
        form = ContactUsForm(data=request.POST, instance=contacts)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/message/list/')

    elif request.method == 'GET':
        form = ContactUsForm(instance=contacts)

    context2 = {
        'form': form
    }

    return render(request, 'contactUs_update.html', context2)


def source_update(request, pk):
    source = get_object_or_404(Source, id=pk)


    if request.method == 'POST':
        form = RateForm(data=request.POST, instance=source)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')

    elif request.method == 'GET':
        form = SourceForm(instance=source)

    context3 = {
        'form': form
    }

    return render(request, 'source_update.html', context3)


def rate_delete(request, pk):
    rate = get_object_or_404(Rate, id=pk)

    if request.method == 'GET':
        context = {
            'rate': rate
        }
        return render(request, 'rate_delete.html', context)

    elif request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')


def contactUs_delete(request, pk):
    contacts = get_object_or_404(ContactUs, id=pk)

    if request.method == 'GET':
        context = {
            'contacts': contacts
        }
        return render(request, 'contactUs_delete.html', context)

    elif request.method == 'POST':
        contacts.delete()
        return HttpResponseRedirect('/message/list/')


def source_delete(request, pk):
    sources = get_object_or_404(Source, id=pk)

    if request.method == 'GET':
        context = {
            'sources': sources
        }
        return render(request, 'source_delete.html', context)

    elif request.method == 'POST':
        sources.delete()
        return HttpResponseRedirect('/source/list/')

def source_details(request, pk):
    sources = get_object_or_404(Source, id=pk)

    context = {
        'sources': sources
    }
    return render(request, 'source_details.html', context)



@csrf_exempt
def request_method(request):
    if request.method == 'GET':
        message = 'Render client form'
    elif request.method == 'POST':
        message = 'Validate form data'

    return HttpResponse(message)
