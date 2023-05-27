import click
from cmd_config import config
from cmd_keystore import create_keystore
from cmd_crosschain import crosschain
from cmd_sp import sp

@click.group()
def gnfd():
    pass


gnfd.add_command(config)
gnfd.add_command(create_keystore, 'create-keystore')
gnfd.add_command(crosschain)
gnfd.add_command(sp)
