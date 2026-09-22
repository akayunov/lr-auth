import base64
import pytest


@pytest.fixture
def text_to_base64url():
    def f(text: str) -> str:
        # 1. Переводим строку в байты (UTF-8)
        text_bytes = text.encode("utf-8")

        # 2. Кодируем в URL-безопасный Base64
        base64url_bytes = base64.urlsafe_b64encode(text_bytes)

        # 3. Декодируем байты обратно в строку и удаляем символы '=' с конца
        return base64url_bytes.decode("utf-8").rstrip("=")

    return f
