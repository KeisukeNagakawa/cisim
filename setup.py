# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cisim',
    version='1.0.1',
    description='Package for simulating confidence interval of Binomial distribution and Hypergeometric distribution',
    # long_description=readme,
    author='Keisuke Nagakawa',
    author_email='kay@amunzen.com',
    install_requires=['numpy', 'scipy', 'cerberus'],
    url='https://github.com/KeisukeNagakawa/cisim',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

