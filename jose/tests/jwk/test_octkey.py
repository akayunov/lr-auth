from unittest import mock

import joserfc
import pytest
from joserfc.jwk import OctKey


def test_octkey(text_to_base64url):
    key_size = 8 * 32
    key = OctKey.generate_key(key_size)
    assert len(key.raw_value) == key_size / 8

    k1 = OctKey.import_key(
        "my-secret-key-bigger-then-112-bits", {"alg": "HS256", "kid": "101"}
    )
    k2 = OctKey.import_key(b"my-secret-key-bigger-then-112-bits", {"use": "sig"})
    k3 = OctKey.import_key(
        {"kty": "oct", "k": text_to_base64url("my-secret-key-bigger-then-112-bits")}
    )

    assert k1.raw_value == k2.raw_value == k3.raw_value
    assert k1.alg == "HS256"
    assert k1.as_dict() == {
        "k": text_to_base64url("my-secret-key-bigger-then-112-bits"),
        "alg": "HS256",
        "kty": "oct",
        "kid": "101",
    }

    with pytest.raises(joserfc.errors.UnsupportedKeyAlgorithmError):
        k1.check_alg("ECDH-EC")
    k2.check_alg("HS256")

    k1.check_key_op("sign")
    k1.check_key_op("encrypt")

    k1.check_use("sig")
    k1.check_use("enc")
    assert k1.dict_value == k1.as_dict()
    k2.ensure_kid()
    assert k2.as_dict()["kid"] == k2.thumbprint()

    assert k1.is_private
    assert k1.private_key == b"my-secret-key-bigger-then-112-bits"
    assert k1.public_key == b"my-secret-key-bigger-then-112-bits"

    assert k1.thumbprint() == "sVZoqX2Y1oXgasZCdpdt--lnys-VC96Y4TZqnz17rus"

    assert (
        k1.thumbprint_uri()
        == "urn:ietf:params:oauth:jwk-thumbprint:sha-256:sVZoqX2Y1oXgasZCdpdt--lnys-VC96Y4TZqnz17rus"
    )
