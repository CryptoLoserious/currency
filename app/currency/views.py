# from time import time

# from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
# from django.contrib.auth import get_user_model
from currency.models import Rate, ContactUs, Source
from django.core.mail import send_mail
from django.urls import reverse_lazy
from currency.forms import RateForm, SourceForm, ContactUsForm
from django.views.generic import (
    ListView, CreateView,
    UpdateView, DeleteView,
    DetailView, TemplateView
)


class RateListView(UserPassesTestMixin, ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'

    def test_func(self):
        return self.request.user.is_superuser


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contactUs.html'


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


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

    # def dispatch(self, request, *args, **kwargs):
    #     start = time()
    #
    #     response = super().dispatch(request, *args, **kwargs)
    #
    #     end = time()
    #
    #     # print(f'After view: {end - start}')
    #     return response

    def _send_email(self):
        from django.conf import settings
        recipient = settings.DEFAULT_FROM_EMAIL
        subject = 'User contact us'
        body = f'''
            Name: {self.object.name}
            Email: {self.object.email_from}
            Subject: {self.object.subject}
            Body: {self.object.body}
            '''

        send_mail(
            subject,
            body,
            recipient,
            [recipient],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)

        self._send_email()

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
