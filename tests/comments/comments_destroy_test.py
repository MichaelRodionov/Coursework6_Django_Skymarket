import pytest


# ----------------------------------------------------------------
# advertisement retrieve view test
@pytest.mark.django_db
def test_destroy_comment(client, advertisement, comment, test_auth_data):
    auth_token = test_auth_data[0]

    response = client.delete(
        f'/api/ads/{advertisement.pk}/comments/{comment.pk}/',
        HTTP_AUTHORIZATION='Bearer ' + auth_token
    )

    assert response.status_code == 204, 'Status code error'
    assert response.data is None, 'Wrong response'


# ----------------------------------------------------------------
@pytest.mark.django_db
def test_retrieve_comment_401(client, comment, advertisement, test_auth_data):
    response = client.get(
        f'/api/ads/{advertisement.pk}/comments/{comment.pk}/',
    )

    expected_response: dict = {
        'detail': 'Учетные данные не были предоставлены.'
    }

    assert response.status_code == 401, 'Status code error'
    assert response.data is not None, 'HttpResponseError'
    assert response.data == expected_response, 'Wrong data expected'
