# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Package for simulationg confidence interval of Binomial distribution and Hypergemetric distribution',
    long_description=readme,
    author='Keisuke Nagakawa',
    author_email='kay@amunzen.com',
    install_requires=['numpy', 'scipy'],
    url='https://github.com/KeisukeNagakawa/cisim',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

