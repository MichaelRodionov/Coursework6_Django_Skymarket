import pytest


# ----------------------------------------------------------------
# advertisement retrieve view test
@pytest.mark.django_db
def test_retrieve_ad(client, advertisement, test_auth_data):
    auth_token = test_auth_data[0]
    user = test_auth_data[1]

    response = client.get(
        f'/api/ads/{advertisement.pk}/',
        HTTP_AUTHORIZATION='Bearer ' + auth_token
    )
    print(f'response1= {response.data}')
    expected_response: dict = {
        "pk": response.data.get('pk'),
        "title": 'test_advertisement',
        "description": 'test_description',
        "price": 999,
        "phone": user.phone,
        # "author_id": response.data.get('pk'),
        "author_id": 7,
        "author_first_name": user.first_name,
        "author_last_name": user.last_name,
        "image": None
    }
    print(f'response2= {response.data}')
    print(f'expected_response= {expected_response}')
    assert response.status_code == 200, 'Status code error'
    assert response.data is not None, 'HttpResponseError'
    assert response.data == expected_response, 'Wrong data expected'


# ----------------------------------------------------------------
@pytest.mark.django_db
def test_retrieve_ad_401(client, advertisement, test_auth_data):
    response = client.get(
        f'/api/ads/{advertisement.pk}/',
    )

    expected_response: dict = {
        'detail': 'Учетные данные не были предоставлены.'
    }

    assert response.status_code == 401, 'Status code error'
    assert response.data is not None, 'HttpResponseError'
    assert response.data == expected_response, 'Wrong data expected'
