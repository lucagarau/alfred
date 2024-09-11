from setuptools import setup, find_packages

setup(
    name='alfred_bot',
    version='2.0',
    author='Mr.Liuk',
    description='Un semplice bot per telegram per aiutare i batcavernicoli',
    packages=find_packages(),
    install_requires=[
        'telebot',
    ],
)
