import base64
import requests

def test_basic_auth_code_grant_type_public_client():
    # no client secret
    requests.post(
        "/token",
        data={
            "grant_type": "authorization_code",
            "code": "access_code",
            "client_id": "some_client_id",
        }
    )


def test_basic_auth_code_grant_type_private_client_post_client_auth():
    # no client secret
    requests.post(
        "/token",
        data={
            "grant_type": "authorization_code",
            "code": "access_code",
            "client_id": "some_client_id",
            "client_secret": "some_client_secret",
        }
    )

def test_basic_auth_code_grant_type_private_client_basic_client_auth():
    # no client secret
    requests.post(
        "/token",
        headers={'Authorization': f'Basic {base64.b64encode(b"some_client_id")}:{base64.b64encode(b"some_client_secret")}'},
        data={
            "grant_type": "authorization_code",
            "code": "access_code",
            "client_id": "some_client_id",
            "client_secret": "some_client_secret",
        }
    )

