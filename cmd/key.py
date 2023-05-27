import json
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from eth_account import Account


class Key:
    def __init__(self, address, private_key):
        self.address = address
        self.privateKey = private_key


class EncryptedKey:
    def __init__(self, address, crypto):
        self.address = address
        self.crypto = crypto


def format_private_key(private_key):
    if private_key.startswith('0x'):
        private_key = private_key[2:]  # Remove '0x' prefix
    return private_key


def encrypt_key(key, auth, scrypt_n, scrypt_p):
    key_bytes = bytes.fromhex(key.privateKey)
    salt = get_random_bytes(32)
    derived_key = scrypt(auth.encode(), salt, 32, N=scrypt_n, r=8, p=scrypt_p)
    iv = get_random_bytes(16)
    cipher = AES.new(derived_key[:16], AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(key_bytes, AES.block_size))
    crypto_struct = {
        "ciphertext": b64encode(ciphertext).decode(),
        "cipherparams": {"iv": b64encode(iv).decode()},
        "kdf": "scrypt",
        "kdfparams": {
            "salt": b64encode(salt).decode(),
            "n": scrypt_n,
            "r": 8,
            "p": scrypt_p
        },
        "mac": ""
    }
    encrypted_key = EncryptedKey(key.address, crypto_struct)
    return json.dumps(encrypted_key.__dict__)


def decrypt_key(key_json, auth):
    key_data = json.loads(key_json)
    key_bytes = Account.decrypt(key_data['crypto'], auth)
    return key_bytes.hex()
