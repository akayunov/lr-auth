from joserfc import jwk


def test_basic(text_to_base64url):
    b64_secret_key = text_to_base64url("my-secret_key")
    k1 = jwk.import_key(
        {
            "kty": "oct",
            "k": b64_secret_key,
            "use": "sig",
        }
    )

    k2 = jwk.import_key("my-secret_key", "oct")

    k3 = jwk.OctKey.import_key("my-secret_key")

    assert k1.raw_value == k2.raw_value
    assert k1.raw_value == k3.raw_value

    rsa1 = jwk.generate_key("RSA", 2048, {"use": "sig"})
    # same as:
    rsa2 = jwk.RSAKey.generate_key(2048, {"use": "sig"})
    assert rsa1.as_dict()["e"] == rsa2.as_dict()["e"] == "AQAB"
