import json

from web3 import Web3, Account

from key import decrypt_key
from load import ctx
from utils import get_password, parse_config_file


def new_client():
    config = parse_config_file('../.env')

    rpc_addr = config.RpcAddr
    if not rpc_addr:
        raise ValueError("Failed to parse rpc address. Please set it in the config file.")

    chain_id = config.ChainId
    if not chain_id:
        raise ValueError("Failed to parse chain id. Please set it in the config file.")

    key_file = "../key.json"  # Specify the path to your keystore file
    with open(key_file, "r") as file:
        key_data = json.load(file)

    password = get_password(config)
    private_key = decrypt_key(key_data, password[0])

    account = Account.from_key(private_key)

    host = config.Host

    client = ctx.call(f"Client.create({rpc_addr}, {chain_id})")

    return client


def parse_bucket_and_object(url_path):
    if "gnfd://" in url_path:
        url_path = url_path[len("gnfd://"):]

    index = url_path.find("/")

    if index == -1:
        raise ValueError("URL not correct, cannot parse bucket name and object name")

    return url_path[:index], url_path[index + 1:]


def parse_bucket(url_path):
    if "gnfd://" in url_path:
        url_path = url_path.replace("gnfd://", "")

    splits = url_path.split("/", 1)

    return splits[0]
