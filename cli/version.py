import os
from pathlib import Path

__version__ = '0.2.0-dev'
PROGRAM_NAME = 'pbwt cli'

venv_path = os.environ.get('VIRTUAL_ENV', os.path.join('..', 'venv'))
ROOT_DIR = Path(os.path.join(venv_path, '..')).resolve()
