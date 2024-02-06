import re

from django.contrib.auth.mixins import UserPassesTestMixin
from currency.models import Rate, ContactUs, Source
from django_filters.views import FilterView
from django.urls import reverse_lazy
from currency.forms import RateForm, SourceForm, ContactUsForm
from django.views.generic import (
    CreateView,
    UpdateView, DeleteView,
    DetailView, TemplateView
)

from currency.tasks import send_email_in_background

from currency.filters import RateFilter, ContactUsFilter, SourceFilter


class RateListView(UserPassesTestMixin, FilterView):
    queryset = Rate.objects.all().select_related('source').order_by('-created')
    template_name = 'rate_list.html'
    paginate_by = 10
    filterset_class = RateFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        query_parameters = self.request.GET.urlencode()

        context['filter_params'] = re.sub(r'page=\d+', '', query_parameters).lstrip('&')

        return context

    def test_func(self):
        return self.request.user.is_active


class ContactUsListView(FilterView):
    queryset = ContactUs.objects.all().order_by('-created')
    template_name = 'contactUs.html'
    paginate_by = 10
    filterset_class = ContactUsFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        query_parameters = self.request.GET.urlencode()

        context['filter_params'] = re.sub(r'page=\d+', '', query_parameters).lstrip('&')

        return context


class SourceListView(FilterView):
    queryset = Source.objects.all().order_by('-created')
    template_name = 'source_list.html'
    paginate_by = 10
    filterset_class = SourceFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        query_parameters = self.request.GET.urlencode()

        context['filter_params'] = re.sub(r'page=\d+', '', query_parameters).lstrip('&')

        return context


class RateCreateView(UserPassesTestMixin, CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'

    def test_func(self):
        return self.request.user.is_superuser


class ContactUsCreateView(CreateView):
    model = ContactUs
    template_name = 'contactUs_create.html'
    success_url = reverse_lazy('index')
    fields = (
        'name',
        'email_from',
        'subject',
        'body'
    )

    def _send_email(self):
        # from django.conf import settings
        # recipient = settings.DEFAULT_FROM_EMAIL
        subject = 'User contact us'
        body = f'''
                Name: {self.object.name}
                Email: {self.object.email_from}
                Subject: {self.object.subject}
                Body: {self.object.body}
                '''
        # eta = datetime.now() + timedelta(seconds=60)

        send_email_in_background(
            **{
                'subject': subject,
                'body': body
            }
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)

        self._send_email()
        # breakpoint()

        return redirect


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
