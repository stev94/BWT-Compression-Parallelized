import version

from setuptools import setup

requirements = [
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
    py_modules=['pbwt'],
    install_requires=requirements,
    entry_points={'console_scripts': ['pbwt=pbwt:cli']}
)
