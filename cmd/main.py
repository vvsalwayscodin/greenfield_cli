import click
from cmd_config import config


@click.group()
def gnfd():
    pass


gnfd.add_command(config)

