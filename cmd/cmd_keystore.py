import click


@click.command()
@click.option('--privKeyFile', type=str, help="Generate keystore example.json",
              prompt="Enter path to privateKeyFile and name generating json file | gnfd create_keystore ./key.txt key.json")
def create_keystore(privKeyFile):
    click.echo(privKeyFile)
