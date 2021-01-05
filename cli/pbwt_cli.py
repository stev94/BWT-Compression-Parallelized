import os
import click
import subprocess
from cli import version

@click.group()
@click.pass_context
@click.version_option(version=version.__version__, prog_name=version.PROGRAM_NAME)
def cli():
    """
    A command line interface for PBWT.
    """
    pass


@cli.command('zip')
@click.argument('INPUT_FILE', type=click.Path(exists=True))
@click.argument('OUTPUT_FILE', type=click.Path())
@click.option('--chunk_size', type=float, help='Chunk size in MB. Max = 5 MB. Default = 0.9 MB.', default=0.9)
@click.option('--mode', type=str, help="Run PBWT in parallel (p) or in single thread (s). Default 'p'.", default='p')
def zip_(input_file, output_file, chunk_size, mode):
    subprocess.call([os.path.join(version.ROOT_DIR, 'bin', 'pbwt'),
                     'zip', input_file, output_file, str(chunk_size), mode])


@cli.command('unzip')
@click.argument('INPUT_FILE', type=click.Path(exists=True))
@click.argument('OUTPUT_FILE', type=click.Path())
def unzip(input_file, output_file):
    subprocess.call([os.path.join(version.ROOT_DIR, 'bin', 'pbwt'),
                     'unzip', input_file, output_file])


@cli.command('compare')
@click.argument('FILE1', type=click.Path(exists=True))
@click.argument('FILE2', type=click.Path(exists=True))
def compare(file1, file2):
    subprocess.call([os.path.join(version.ROOT_DIR, 'bin', 'pbwt'),
                     'compare', file1, file2])


if __name__ == '__main__':
    cli()
