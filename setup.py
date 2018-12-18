#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='mailprinter',
    author='Abhyudaya Sharma',
    author_email='sharmaabhyudaya@gmail.com',
    description='Print by sending an email',
    packages=find_packages(),
    package_data={'': ['config.json']},
    install_requires=['pycups', 'schedule'],
    include_package_data=True,
    license='MIT'
)

