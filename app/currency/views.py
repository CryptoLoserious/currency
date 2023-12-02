from currency.models import Rate, ContactUs, Source
from django.urls import reverse_lazy
from currency.forms import RateForm, SourceForm, ContactUsForm
from django.views.generic import (
    ListView, CreateView,
    UpdateView, DeleteView,
    DetailView, TemplateView
)


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contactUs.html'


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


class ContactUsCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('currency:message-list')
    template_name = 'contactUs_create.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_create.html'


class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'


class ContactUsUpdateView(UpdateView):
    model = ContactUs
    form_class = ContactUsForm
    success_url = reverse_lazy('currency:message-list')
    template_name = 'contactUs_update.html'


class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_update.html'


class RateDeleteView(DeleteView):
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_delete.html'


class ContactUsDeleteView(DeleteView):
    model = Rate
    success_url = reverse_lazy('currency:message-list')
    template_name = 'contactUs_delete.html'


class SourceDeleteView(DeleteView):
    model = Source
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_delete.html'


class RateDetailView(DetailView):
    model = Rate
    template_name = 'rate_details.html'


class IndexView(TemplateView):
    template_name = 'index.html'
