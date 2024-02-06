from django.urls import reverse
# from django.conf import settings
#
# from currency.models import Source


def test_post_source_empty_form_200(client):
    response = client.post(reverse('currency:source-create'))
    assert response.status_code == 200
    # breakpoint()


def test_post_source_empty_form_errors(client):
    response = client.post(reverse('currency:source-create'))
    assert response.context_data['form'].errors == {
        'source_url': ['This field is required.'],
        'name': ['This field is required.']
    }


def test_post_source_invalid_url(client):
    payload = {
        'name': 'Name',
        'url': 'INVALID_URL',
    }
    response = client.post(reverse('currency:source-create'), data=payload)
    assert response.status_code == 200
    # breakpoint()
    assert response.context_data['form'].errors == {
        'source_url': ['This field is required.']
    }


def test_post_source_valid_data(client):
    # initial_count = Source.objects.count()
    payload = {
        'name': 'Name',
        'url': 'urlexample.com',
    }

    response = client.post(reverse('currency:contact-create'), data=payload)
    assert response.status_code == 200
    # assert response.headers['Location'] == '/'
    # assert len(mailoutbox) == 1
    # assert mailoutbox[0].from_email == settings.DEFAULT_FROM_EMAIL
    # assert Source.objects.count() == initial_count + 1
