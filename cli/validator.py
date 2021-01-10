import os
import click

from cli.util import create_error
from cli.constants import *


def _check_file_exists(file, del_out_flag):
    if os.path.exists(file):
        if del_out_flag:
            os.remove(file)
        elif click.confirm(OVERWRITE_FILE.format(file), abort=True):
            os.remove(file)


def _check_output_file(input_file, output_file, new_extension, del_out_flag):
    if output_file is None:
        output_file = f'{input_file.split(".")[0]}.{new_extension}'
    _check_file_exists(output_file, del_out_flag)
    return output_file


def validate_zip(input_file, output_file, del_out_flag):
    return _check_output_file(input_file, output_file, 'pbwt', del_out_flag)


def validate_unzip(input_file, output_file, del_out_flag):
    if not input_file.endswith('.pbwt'):
        create_error(msg, InputError(UNZIP_INPUT_FILE_ERROR))
    return _check_output_file(input_file, output_file, 'unpbwt', del_out_flag)
