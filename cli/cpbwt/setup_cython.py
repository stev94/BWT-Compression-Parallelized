import os
import glob
import version_cython as version

from setuptools import setup, Extension
from Cython.Build import cythonize

source_dir = os.path.join(version.ROOT_DIR, 'src', 'sources')
extension = Extension('*',
                      sources=['*.pyx',
                               *glob.glob(os.path.join(source_dir, "*.c"))],
                      include_dirs=[os.path.join(version.ROOT_DIR, 'src', 'headers')])
ext_modules = cythonize(extension,
                        build_dir=os.path.join(version.ROOT_DIR, "build", "cpypbwt"),
                        annotate=True, compiler_directives={"profile": True})

requirements = [
    'cython==0.29.21',
    'click==7.1.2',
    'pyyaml==5.3'
]

setup(
    name=version.PROGRAM_NAME,
    version=version.__version__,
    author='Stefano Valladares',
    author_email='stefano.valladares12@gmail.com',
    description='A Cython cli for the pbwt C applications',
    url='https://github.com/stev94/Parallel-BWT-Compression',
    python_requires='>=3.8',
    py_modules=['pbwt_cli'],
    install_requires=requirements,
    package_dir={'': os.path.join(version.ROOT_DIR, 'build', 'cpypbwt')},
    entry_points={'console_scripts': ['pbwt=pbwt:cli']},
    ext_modules=ext_modules
)
