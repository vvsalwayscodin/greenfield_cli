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


def encrypt_key(key, auth):
    private_key = format_private_key(key.privateKey)
    key_bytes = bytes.fromhex(private_key)
    encrypted_data = Account.encrypt(key_bytes, auth)
    key_json = EncryptedKey(key.address, encrypted_data)
    return json.dumps(key_json.__dict__)

def decrypt_key(key_json, auth):
    key_data = json.loads(key_json)
    key_bytes = Account.decrypt(key_data['crypto'], auth)
    return key_bytes.hex()
