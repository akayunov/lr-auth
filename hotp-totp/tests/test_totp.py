import time
import qrcode

from otpauth import TOTP

def test_hotp():
    totp = TOTP(b'my-secret')
    code = totp.generate()
    assert totp.verify(code)
    time.sleep(31)
    assert not totp.verify(code)


def test_qr_code():
    totp = TOTP(b'my-secret')
    uri = totp.to_uri(label='Application label', issuer='AK')
    assert uri == "otpauth://totp/Application%20label?secret=NV4S243FMNZGK5A&issuer=AK&algorithm=SHA1&digits=6&period=30"

    # 2. Создаем объект QR-кода
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(uri)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("totp_qr.png")
