import os
import shutil

# folders
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
COMPRESSORS_BIN = os.path.join(ROOT_DIR, 'compressors')
RES_DIR = os.path.join(ROOT_DIR, 'results')
ZIP_DIR = os.path.join(ROOT_DIR, 'zips')


def create_dir(directory, remove=True):
    if os.path.exists(directory):
        if not remove:
            print(f'The directory {directory} already exists and you ask not to delete it.')
            return
        shutil.rmtree(directory)
    os.mkdir(directory)


COMPRESSORS = [
    'pbwt',
    # 'zip',
]

BENCHMARKS = {
    # 'canterbury': {
    #     'url': 'https://corpus.canterbury.ac.nz/resources/cantrbry.zip',
    #     'descr': 'This collection was developed in 1997 as an improved version '
    #              'of the Calgary corpus. The files were chosen because their '
    #              'results on existing compression algorithms are "typical", and '
    #              'so it is hoped this will also be true for new methods.'
    # },
    'artificial': {
        'url': 'https://corpus.canterbury.ac.nz/resources/artificl.zip',
        'descr': 'This collection contains files for which the compression '
                 'methods may exhibit pathological or worst-case behaviour.'
    },
    # 'large': {
    #     'url': 'https://corpus.canterbury.ac.nz/resources/large.zip',
    #     'descr': 'This is a collection of relatively large files.'
    # },
    # 'misc': {
    #     'url': 'https://corpus.canterbury.ac.nz/resources/misc.zip',
    #     'descr': 'This is a collection of "miscellaneous" files that is designed'
    #              ' to be added to by researchers and others wishing to publish '
    #              'compression results using their own files.'
    # },
    # 'calgary': {
    #     'url': 'https://corpus.canterbury.ac.nz/resources/calgary.zip',
    #     'descr': 'his was developed in the late 1980s, and during the 1990s '
    #              'became something of a de facto standard for lossless '
    #              'compression evaluation. The collection is now rather dated, '
    #              'but it is still reasonably reliable as a performance indicator. '
    # },
    # 'silesia': {
    #     'url': 'http://sun.aei.polsl.pl/~sdeor/corpus/silesia.zip',
    #     'descr': 'The intention of the Silesia corpus is to provide a data set '
    #              'of files that covers the typical data types used nowadays. The'
    #              ' sizes of the files are between 6 MB and 51 MB.'
    # }
}
