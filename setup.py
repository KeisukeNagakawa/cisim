# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('PyPIDescription.rst') as f:
    desc = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cisim',
    version='1.0.9.1',
    description='Package for simulating confidence interval of Binomial distribution and Hypergeometric distribution',
    long_description=desc,
    long_description_content_type='text/x-rst',
    author='Keisuke Nagakawa',
    author_email='keisuke.n.37@gmail.com',
    install_requires=['numpy', 'scipy', 'cerberus'],
    url='https://github.com/KeisukeNagakawa/cisim',
    license="MIT",
    packages=find_packages(exclude=('tests', 'docs'))
)

