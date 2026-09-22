from joserfc.jwk import RSAKey, ECKey, KeySetSerialization

def test_key_serialization():
    rsakey1 = RSAKey.generate_key(2048, {'alg': 'RS256'})
    eckey1 = ECKey.generate_key("P-256")
    key_dict = KeySetSerialization.fromkeys([1,2], [rsakey1, eckey1])
    assert list(key_dict.keys()) == [1,2]