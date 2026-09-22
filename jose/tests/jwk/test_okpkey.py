from joserfc.jwk import OKPKey


def test_okpkey():
    key = OKPKey.generate_key("Ed25519")

    pem_file = """
    -----BEGIN PRIVATE KEY-----
    MEcCAQAwBQYDK2VxBDsEOaVsPKMXOBfq9aHlDEaMlBY+FR63hwrINHa2X74uHXUr
    3/VXE8eMhrr8stXn41CQKqVmFEeL5Uj5Gg==
    -----END PRIVATE KEY-----
    """

    OKPKey.import_key(pem_file)
    OKPKey.import_key({
        "kty": "OKP",
        "crv": "Ed25519",
        "x": "t-nFRaxyM5DZcpg5lxiEeJcZpMRB8JgcKaQC0HRefXU",
        "d": "gUF17HCe-pbN7Ej2rDSXl-e7uSj7rQW5u2dNu0KINP0",
        "kid": "5V_IcL-iX5IbaNz9vg0CjXtWLZiJ94-ESnHI-HN1L2Y"
    })
    OKPKey.derive_key("your-secret-key", "Ed25519")
    OKPKey.derive_key("your-secret-key", "Ed25519", kdf_name="HKDF")