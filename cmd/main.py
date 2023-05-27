import click

from cmd_bank import bank
from cmd_bucket import bucket
from cmd_config import config
from cmd_crosschain import crosschain
from cmd_group import group
from cmd_keystore import create_keystore
from cmd_object import policy, object
from cmd_payment import payment
from cmd_sp import sp


@click.group()
def gnfd():
    pass


gnfd.add_command(config)
gnfd.add_command(create_keystore, 'create-keystore')
gnfd.add_command(crosschain)
gnfd.add_command(sp)
gnfd.add_command(bucket)
gnfd.add_command(payment)
gnfd.add_command(bank)
gnfd.add_command(policy)
gnfd.add_command(object)
gnfd.add_command(group)
