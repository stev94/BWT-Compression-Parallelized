import click

from cli.constants import PREFIX_MSG


def create_msg(msg, error=False):
    click.echo(PREFIX_MSG + msg, err=error)


def create_error(msg, exception):
    create_msg(msg, error=True)
    raise exception
