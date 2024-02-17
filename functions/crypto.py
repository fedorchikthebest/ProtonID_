import gostcrypto
import base64


def b64encrypt(data: str, key: str, init_vect: str) -> str:

    key = bytearray(key.encode())

    plain_text = bytearray(str(data).encode())

    cipher_obj = gostcrypto.gostcipher.new('kuznechik',
                                           key,
                                           gostcrypto.gostcipher.MODE_CBC,
                                           init_vect=bytearray(init_vect.encode()))

    cipher_text = cipher_obj.encrypt(plain_text)

    return base64.b64encode(cipher_text).decode()


def b64decrypt(data: str, key: str, init_vect: str) -> str:

    key = bytearray(key.encode())

    plain_text = bytearray(base64.b64decode(data))

    cipher_obj = gostcrypto.gostcipher.new('kuznechik',
                                           key,
                                           gostcrypto.gostcipher.MODE_CBC,
                                           init_vect=bytearray(init_vect.encode()))

    decrypt_text = cipher_obj.decrypt(plain_text)

    return decrypt_text.replace(b'\x00', b'').decode()