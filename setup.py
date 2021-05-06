#!/usr/bin/env python

from setuptools import find_packages, setup

AUTHOR = "S. Stanton"
NAME = "upcycle"
PACKAGES = find_packages()

setup(
    name=NAME,
    version='0.0.1',
    description='Reusable code snippets',
    author=AUTHOR,
    author_email='ss13641@nyu.edu',
    url='https://github.com/samuelstanton/upcycle',
    packages=PACKAGES,
)
