import os


# folders
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
COMPRESSORS_BIN = os.path.join(ROOT_DIR, 'compressors')
ZIP_DIR = os.path.join(ROOT_DIR, 'zips')

BENCHMARKS_URLS = []

COMPRESSORS = [
    'pbwt',
    'zip',
]
