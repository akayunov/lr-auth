from unittest import mock

import requests
from joserfc.jwk import KeySet


def test_keyset():
    key_set = KeySet.generate_key_set("EC", "P-256", count=4)

    assert key_set.as_dict() == {'keys': [{'crv': 'P-256', 'kid': mock.ANY, 'kty': 'EC', 'x': mock.ANY, 'y': mock.ANY},
                                          {'crv': 'P-256', 'kid': mock.ANY, 'kty': 'EC', 'x': mock.ANY, 'y': mock.ANY},
                                          {'crv': 'P-256', 'kid': mock.ANY, 'kty': 'EC', 'x': mock.ANY, 'y': mock.ANY},
                                          {'crv': 'P-256', 'kid': mock.ANY, 'kty': 'EC', 'x': mock.ANY, 'y': mock.ANY}]}


def test_url_import():
    pass
    # resp = requests.get("https://example.com/jwks.json")
    # key_set = KeySet.import_key_set(resp.json())
    # assert len(key_set) == 4


def test_json_import():
    pass
    #
    # with open("your-jwks.json") as f:
    #     data = json.load(f)
    #     key_set = KeySet.import_key_set(data)