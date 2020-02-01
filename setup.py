# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()


setup(
    name='',
    version='0.1.0',
    description='Task',
    long_description=readme,
    author='Velin Vangelov',
    author_email='velin.br.vangelov@gmail.com',
    url='https://github.com/kryptikko',
    packages=find_packages(exclude=('tests', 'docs'))
)

