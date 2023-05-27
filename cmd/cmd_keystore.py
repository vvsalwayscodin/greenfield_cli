import click


@click.command()
@click.option('-pkf', '--private_key_file', default='../key.txt', help='Private key file path')
@click.argument('new_file_name')
def create_keystore(private_key_file, new_file_name):
    click.echo(f"{private_key_file}")
