import base64
from urllib.parse import unquote

from Crypto.Cipher import AES

from config import settings


def encrypt(plaintext: str, key_b64: str = None, iv_b64: str = None) -> str:
    key_b64 = key_b64 or settings.GATEWAY_KEY
    iv_b64 = iv_b64 or settings.GATEWAY_IV
    key = base64.b64decode(key_b64)
    iv = base64.b64decode(iv_b64)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
    encrypted = cipher.encrypt(plaintext.encode("utf-8"))
    b64_str = base64.b64encode(encrypted).decode("utf-8")
    return b64_str.replace("+", "$").replace("=", "*")


def decrypt(encrypted_str: str, key_b64: str = None, iv_b64: str = None) -> str:
    if not encrypted_str:
        return ""
    key_b64 = key_b64 or settings.GATEWAY_KEY
    iv_b64 = iv_b64 or settings.GATEWAY_IV
    encrypted_str = unquote(encrypted_str).replace("*", "=").replace("$", "+")
    key = base64.b64decode(key_b64)
    iv = base64.b64decode(iv_b64)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_str))
    return decrypted.decode("utf-8")
