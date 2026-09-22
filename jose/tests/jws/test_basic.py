from joserfc import jws
from joserfc.jwk import OctKey


def test_jws_basic():
    key = OctKey.generate_key(256)
    token = jws.serialize_compact({"alg": "HS256"}, 'secret-data', key)
    assert token.startswith('e')

    data = jws.deserialize_compact(token, key)
    assert data.protected['alg'] == 'HS256'
    assert data.payload == b'secret-data'
