import version

from setuptools import setup

setup(
    name=version.PROGRAM_NAME,
    version=version.__version__,
    author='Stefano Valladares',
    author_email='stefano.valladares12@gmail.com',
    description='A Cython cli for the pbwt C applications',
    url='https://github.com/stev94/Parallel-BWT-Compression',
    python_requires='>=3.8',
    py_modules=['pbwt'],
    install_requires=['Click==7.1.2'],
    entry_points={'console_scripts': ['pbwt=cli.pbwt:cli']}
)
