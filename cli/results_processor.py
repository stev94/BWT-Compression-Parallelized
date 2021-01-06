import os

from cli.util import create_msg


def _process_zip_results(stdout, input_file, output_file):
    exec_time = float(stdout.split('execution_time = ')[1].split(' -')[0])
    chunk_size = float(stdout.split('chunk_size = ')[1].split('.')[0])

    input_size = os.path.getsize(input_file)
    output_size = os.path.getsize(output_file)
    n_chunks = int(input_size / chunk_size) + 1
    deflated = (1 - (output_size / input_size)) * 100

    create_msg(f'The file has been divided in {n_chunks} chunks before compression.')
    create_msg(f'Time for compression is {exec_time} seconds.')
    create_msg(f'Original size: {input_size}. Compressed size: {output_size}.'
               f' Deflated: {deflated:.1f}%')


def _process_compare_results(stdout):
    if 'are not equal' in stdout:
        create_msg('Files are not equal.')
    else:
        create_msg('Files are equal')


def process_results(stdout, *args):
    action = stdout.split('Starting ')[1].split('...')[0]
    if action == 'zip':
        _process_zip_results(stdout, *args)
    elif action == 'unzip':
        exec_time = float(stdout.split('execution_time = ')[1].split(' -')[0])
        create_msg(f'Unzip terminated successfully in {exec_time} seconds.')
    elif action == 'comparison':
        _process_compare_results(stdout)
    else:
        raise ValueError("The read action is not available. How the fuck could this happen?!")
