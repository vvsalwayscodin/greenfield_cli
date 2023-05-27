import click

from client_gnfd import new_client


@click.group('payment')
def payment():
    pass


@click.command('create_account')
def create_account():
    try:
        w3 = new_client(ctx)

        account_address = w3.eth.default_account

        tx_hash = w3.create_payment_account(account_address,
                                            {})  # Replace with the actual method to create a payment account

        receipt = w3.eth.waitForTransactionReceipt(tx_hash)

        if receipt is not None and receipt["status"] == 1:
            print(f"Create payment account for {account_address} successful, txHash: {tx_hash.hex()}")
        else:
            print("Failed to create payment account.")
    except Exception as e:
        print(f"Error creating payment account: {str(e)}")


@click.command('deposit')
@click.option('--to_address', type=str, help="the stream account", prompt='Enter the stream account')
@click.option('--amount', type=str, help="the amount to be deposited", default="",
              prompt='Enter the amount to be deposited')
def deposit(to_address, amount):
    click.echo(f"{amount}")


@click.command('withdraw')
@click.option('--from_address', type=str, help="the stream account", prompt='Enter the stream account')
@click.option('--amount', type=str, help="the amount to be deposited", default="",
              prompt='Enter the amount to be deposited')
def withdraw(from_address, amount):
    click.echo(f"{amount}")


@click.command('ls')
@click.option('--owner_address', type=str, default="",
              help="indicate a owner's payment accounts to be list, account address can be omitted for current user's accounts listing",
              required=False)
def ls(owner_address):
    click.echo(f"{owner_address}")


@click.command('buy-quota')
@click.option('--charged_quota', type=str, help="indicate the target quota to be set for the bucket",
              prompt='Enter the target quota to be set for the bucket')
@click.argument('bucket_url')
def buy_quota(charged_quota, bucket_url):
    click.echo(f"{charged_quota}")


@click.command('quota-info')
@click.argument('bucket_url')
def quota_info(bucket_url):
    click.echo(f"{bucket_url}")


payment.add_command(create_account)
payment.add_command(deposit)
payment.add_command(withdraw)
payment.add_command(ls)
payment.add_command(buy_quota)
payment.add_command(quota_info)
