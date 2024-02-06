from django.urls import reverse
from currency.models import ContactUs
from django.conf import settings


def test_post_contact_us_empty_form_200(client):
    response = client.post(reverse('currency:contact-create'))
    assert response.status_code == 200
    # breakpoint()


def test_post_contact_us_empty_form_errors(client):
    response = client.post(reverse('currency:contact-create'))
    assert response.context_data['form'].errors == {
        'name': ['This field is required.'],
        'email_from': ['This field is required.'],
        'subject': ['This field is required.'],
        'body': ['This field is required.'],
    }


def test_post_contact_us_invalid_email(client):
    payload = {
        'name': 'Name',
        'email': 'INVALID_EMAIL',
        'subject': 'Subject',
        'body': 'Body',
    }
    response = client.post(reverse('currency:contact-create'), data=payload)
    assert response.status_code == 200
    # breakpoint()
    assert response.context_data['form'].errors == {
        'email_from': ['This field is required.']
    }


def test_post_contact_us_valid_data(client, mailoutbox):
    initial_count = ContactUs.objects.count()
    payload = {
        'name': 'Name',
        'email_from': 'email@example.com',
        'subject': 'Subject',
        'body': 'Body',
    }
    response = client.post(reverse('currency:contact-create'), data=payload)
    assert response.status_code == 302
    # breakpoint()
    assert response.headers['Location'] == '/'
    assert len(mailoutbox) == 1
    assert mailoutbox[0].from_email == settings.DEFAULT_FROM_EMAIL
    assert ContactUs.objects.count() == initial_count + 1
