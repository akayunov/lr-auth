from joserfc import jwe
from joserfc.jwk import OctKey


def test_jws_basic():
    protected = {"alg": "A128KW", "enc": "A128GCM"}
    key = OctKey.generate_key(128)  # algorithm requires key of bit size 128
    data = jwe.encrypt_compact(protected, "hello", key)

    obj = jwe.decrypt_compact(data, key)
    assert obj.protected == {"alg": "A128KW", "enc": "A128GCM"}
    assert obj.plaintext == b"hello"
