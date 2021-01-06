import os

from pathlib import Path

# Cli arguments
MIN_CHUNK_SIZE = 0.1        # MegaBytes
MAX_CHUNK_SIZE = 5          # MegaBytes
DEFAULT_CHUNK_SIZE = 0.9    # MegaBytes

RUNNING_MODES = ['parallel', 'sequential']
DEFUALT_RUNNING_MODE = 'parallel'

# Cli Help messages
CHUNK_SIZE_HELP = 'Set the size of the chunk (in MB) in which the file si divided before processing in the range [0.1, 5].'
RUNNING_MODES_HELP = 'Specify if running PBWT in parallel or sequentially. Parallel mode should speed up 2x.'

# files and directoeis
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PBWT_BIN = os.path.join('bin', 'pbwt')

# Messages
PREFIX_MSG = 'PBWT - '

# Error messages
UNZIP_INPUT_FILE_ERROR = 'The input file should have the .pbwt extension'

# Prompt messages
OVERWRITE_FILE = 'The file {} already exists. Do you want to overwrite it?'
