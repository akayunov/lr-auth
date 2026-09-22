from otpauth import HOTP

def test_hotp():
    hotp = HOTP(b'my-secret')
    counter = 4
    code = hotp.generate(counter)
    assert hotp.verify(code, counter)
    assert not hotp.verify(code, counter - 1)
    assert not hotp.verify(code, counter + 1)