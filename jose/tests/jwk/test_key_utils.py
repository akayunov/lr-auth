from joserfc.jwk import ECKey


def test_key_utils():
    eckey = ECKey.generate_key()
    text = eckey.as_der()
    assert len(text) == 91

    text = eckey.as_pem(private=True)
    assert len(text) == 241