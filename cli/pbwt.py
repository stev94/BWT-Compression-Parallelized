import os
import click
import subprocess

from cli import version, validator
from cli.constants import *


@click.group()
@click.pass_context
@click.version_option(version=version.__version__, prog_name=version.PROGRAM_NAME)
def cli(ctx):
    """
    A command line interface for PBWT.
    """
    pass


@cli.command('zip')
@click.argument('INPUT_FILE', type=click.Path(exists=True))
@click.argument('OUTPUT_FILE', type=click.Path(), required=False, default=None)
@click.option('--chunk_size',
              type=click.FloatRange(MIN_CHUNK_SIZE, MAX_CHUNK_SIZE),
              help=CHUNK_SIZE_HELP, default=DEFAULT_CHUNK_SIZE, show_default=True)
@click.option('--mode',
              type=click.Choice(RUNNING_MODES, case_sensitive=False),
              help=RUNNING_MODES_HELP, default=DEFUALT_RUNNING_MODE, show_default=True)
def zip_(input_file, output_file, chunk_size, mode):
    """
    Zip the input file and put the result in the output file.

    \b
    Arguments:
    INPUT_FILE     Path to a valid file to be pbwtzipped.
    [OUTPUT_FILE]  Path to a valid file with extension .pbwt.
                   If not specified, the output will be placed in filename.pbwt
    """
    output_file = validator.validate_zip(input_file, output_file)
    subprocess.call([PBWT_BIN, 'zip', input_file, output_file, str(chunk_size), mode])


@cli.command('unzip')
@click.argument('INPUT_FILE', type=click.Path(exists=True))
@click.argument('OUTPUT_FILE', type=click.Path(), required=False, default=None)
def unzip(input_file, output_file):
    """
    Unzip the input file and put the result in the output file.

    \b
    Arguments:
    INPUT_FILE     Path to a valid file with extension .pbwt to be unpbwtzipped.
    [OUTPUT_FILE]  Path to a valid file with extension .unpbwt.
                   If not specified, the output will be placed in filename.unpbwt
    """
    output_file = validator.validate_unzip(input_file, output_file)
    subprocess.call([PBWT_BIN, 'unzip', input_file, output_file])


@cli.command('compare')
@click.argument('FILE1', type=click.Path(exists=True))
@click.argument('FILE2', type=click.Path(exists=True))
def compare(file1, file2):
    """
    Compare two files. Returns 0 if the files are equal. 1 otherwise.

    \b
    Arguments:
    INPUT_FILE  Path to a valid file with extension .pbwt to be compared.
    OUTPUT_FILE Path to a valid file with extension .pbwt to be compared.
    """
    subprocess.call([PBWT_BIN, 'compare', file1, file2])


if __name__ == '__main__':
    cli()
