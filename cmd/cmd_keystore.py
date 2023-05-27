import json

import click
import os
import errno

from utils import parse_config_file, get_password
from key import encrypt_key, key


@click.command()
@click.option('-pkf', '--private_key_file', default='../key.txt', help='Private key file path')
@click.argument('new_file_name')
def create_keystore(private_key_file, new_file_name):
    key_file_path = '../' + new_file_name

    try:
        os.makedirs(os.path.dirname(key_file_path), mode=0o700)
    except OSError as e:
        if e.errno != errno.EEXIST:
            return "failed to create directory " + os.path.dirname(key_file_path)

    if private_key_file == "":
        return "private key file path"

    # Load private key from file.

    if new_file_name != "":
        config = parse_config_file('../.env')

    password = get_password(config)

    encrypt_content = encrypt_key(key, password[0])

    try:
        with open(key_file_path, "w") as file:
            json.dump(encrypt_content, file)
            file.close()
        return key_file_path
    except IOError as e:
        return "failed to write keyfile to the path " + key_file_path + ": " + str(e)
