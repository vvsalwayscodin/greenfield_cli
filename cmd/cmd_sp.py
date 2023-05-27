import click


@click.group('sp')
def sp():
    pass


@click.command('ls')
def ls():
    click.echo("Storage provider list")


@click.command('head')
@click.argument('URL')
def head(URL):
    click.echo(f"Storage provider info by {URL}")


@click.command('ger-price')
@click.argument('URL')
def get_price(URL):
    click.echo(f"Quota price by {URL}")


sp.add_command(ls)
sp.add_command(head)
sp.add_command(get_price)