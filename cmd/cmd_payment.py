import click


@click.group('payment')
def payment():
    pass


@click.command('create_account')
def create_account():
    click.echo('create account logic')


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
def withdraw(to_address, amount):
    click.echo(f"{amount}")


@click.command('ls')
@click.option('--owner_address', type=str, default="",
              help="indicate a owner's payment accounts to be list, account address can be omitted for current user's accounts listing",
              required=False)
def ls(owner_address):
    click.echo(f"{owner_address}")


payment.add_command(create_account)
payment.add_command(deposit)
payment.add_command(withdraw)
payment.add_command(ls)
