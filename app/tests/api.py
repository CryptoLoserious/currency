from django.urls import reverse


def test_get_rate_list(api_client_auth):
    response = api_client_auth.get(reverse('currency_api:rate-list'))
    assert response.status_code == 200
    assert response.json()


# def test_post_rate_list_empty_body(api_client):
#     response = api_client.post(reverse('currency_api:rate-list'))
#     assert response.status_code == 400
