import click

from client_gnfd import new_client


@click.group('bank')
def bank():
    pass


@click.command('balance')
@click.option('--address', type=str, help="indicate the address's balance to be retrieved",
              prompt="Enter the address's balance to be retrieved")
def balance(address):
    click.echo(f"{address}")


@click.command('transfer')
@click.option('--to_address', type=str, help="the receiver address in BSC", prompt='Enter the receiver address in BSC')
@click.option('--amount', type=str, help="the amount to be sent", default="",
              prompt='Enter the amount to be sent')
def transfer(to_address, amount):
    web3, account = new_client()

    print(web3.eth.accounts)
    click.echo(f"{amount}")


bank.add_command(balance)
bank.add_command(transfer)
