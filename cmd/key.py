import json
from web3 import Web3
from eth_account import Account


class Key:
    def __init__(self, address, private_key):
        self.Address = address
        self.PrivateKey = private_key


class EncryptedKey:
    def __init__(self, address, crypto):
        self.address = address
        self.crypto = crypto


def format_private_key(private_key):
    if private_key.startswith('0x'):
        private_key = private_key[2:]  # Remove '0x' prefix
    return private_key


def encrypt_key(key, auth):
    private_key = format_private_key(key.PrivateKey)
    key_bytes = bytes.fromhex(private_key)
    encrypted_data = Account.encrypt(key_bytes, auth)
    key_json = EncryptedKey(key.Address, encrypted_data)
    return json.dumps(key_json.__dict__)


def decrypt_key(key_json, auth):
    key_data = json.loads(key_json)
    key_bytes = Account.decrypt(key_data['crypto'], auth)
    return key_bytes.hex()


# Usage example
key = Key('',
          '')
auth = ''

encrypted_key_json = encrypt_key(key, auth)
print('Encrypted Key:', encrypted_key_json)

decrypted_private_key = decrypt_key(encrypted_key_json, auth)
print('Decrypted Private Key:', decrypted_private_key)
