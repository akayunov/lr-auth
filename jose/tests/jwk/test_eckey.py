from joserfc.jwk import ECKey


def test_eckey():
    eckey1 = ECKey.generate_key("P-256")

    pem_file = """
    -----BEGIN EC PRIVATE KEY-----
    MHcCAQEEIBnRS4Tf1PY6Jb7QOwAM7OWUOMJTBenEWRvGBCGgctBfoAoGCCqGSM49
    AwEHoUQDQgAE3r15c+Yd+0GXKysfWtwkqF7k12ylNE9LdfRP4TfkUcJSQXyGQjcx
    U8E81rOHjo+9xv2e64n4X6pC3yuP+pX4eA==
    -----END EC PRIVATE KEY-----
    """

    ec2key = ECKey.import_key(pem_file)
    ec3key = ECKey.import_key({
        "kty": "EC",
        "crv": "P-256",
        "x": "WKn-ZIGevcwGIyyrzFoZNBdaq9_TsqzGl96oc0CWuis",
        "y": "y77t-RvAHRKTsSGdIYUfweuOvwrvDD-Q3Hv5J0fSKbE",
        "d": "Hndv7ZZjs_ke8o9zXYo3iq-Yr8SewI5vrqd0pAvEPqg"
    })

    kd1 = ECKey.derive_key("my-secret", "P-256")
    kd2 = ECKey.derive_key("my-secret", "P-256")

    assert kd1.private_key.private_numbers().private_value.to_bytes(32, 'big') == kd2.private_key.private_numbers().private_value.to_bytes(32, 'big')