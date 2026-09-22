import datetime
import json
import uuid

import joserfc
import pytest
from joserfc import jwt, jwk, jwe


def test_basic():
    headers = {'alg': 'HS256'}
    now = datetime.datetime.now(datetime.UTC)
    claim = {'iss': 'me', "iat": now, 'exp': now + datetime.timedelta(minutes=5)}
    key = jwk.OctKey.generate_key(key_size=256, auto_kid=True)
    token = jwt.encode(headers, claim, key)
    assert token.startswith('e')

    token_obj = jwt.decode(token, key, algorithms=['HS256'])
    assert type(token_obj.claims['iat']) is int

    claims_request = jwt.JWTClaimsRegistry(iss={"essential": True, "value": "me"}, iat={"essential": True})

    claims_request.validate(token_obj.claims)
    claims_request = jwt.JWTClaimsRegistry(iss={"essential": True, "value": "xxx"}, iat={"essential": True})

    with pytest.raises(joserfc.errors.InvalidClaimError):
        claims_request.validate(token_obj.claims)


def test_claim_registry():
    class MyCliamRegistry(jwt.JWTClaimsRegistry):
        def validate_my(self, value):
            if value != 'my':
                raise joserfc.errors.InvalidClaimError(f'my field is frong: {value}')

    claims_request = MyCliamRegistry(my={"essential": True})
    with pytest.raises(joserfc.errors.InvalidClaimError):
        claims_request.validate({'my': "me"})


def test_jwe():
    headers = {"alg": "A128KW", "enc": "A128GCM"}
    claims = {"iss": "me", "iat": datetime.datetime.now(datetime.UTC)}
    key = jwk.OctKey.generate_key(key_size=128)
    registry = jwe.JWERegistry()
    encrypted_token = jwt.encode(headers, claims, key, registry=registry)
    assert encrypted_token.startswith('e')


def test_jwt_asymetric():
    key = jwk.RSAKey.generate_key(2048)
    headers = {'alg': 'RS256'}
    now = datetime.datetime.now(datetime.UTC)
    claim = {'iss': 'me', "iat": now, 'exp': now + datetime.timedelta(minutes=5)}
    token = jwt.encode(headers, claim, key)
    assert token.startswith('e')
    token_obj = jwt.decode(token, key)
    assert token_obj.claims['iss'] == 'me'


def test_encode_not_simple_claims():
    class MyEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, uuid.UUID):
                return str(o)
            return super().default(o)

    key = jwk.RSAKey.generate_key(2048)
    claims = {'iss': uuid.uuid4(), 'iat': datetime.datetime.now(datetime.UTC)}
    jwt.encode({"alg": "RS256"}, claims, key, encoder_cls=MyEncoder)