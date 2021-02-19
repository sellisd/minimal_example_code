import click
import importlib.resources as pkg_resources


@click.group()
def me():
    pass


@me.command()
def init():
    sql_script = (pkg_resources.files('me.sql_scripts').joinpath('init.sql').read_text())