#!/usr/bin/env python

import os

from setuptools import setup, find_packages


def path(fname=''):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), fname))


def readfile(fname):
    with open(path(fname)) as f:
        return f.read()


setup(
    name="covid19",
    version="0.1",
    author="Fabio Manganiello",
    author_email="info@fabiomanganiello.com",
    description="CoViD-19 genome analysis tools",
    license="MIT",
    python_requires='>= 3.5',
    packages=find_packages(),
    include_package_data=True,
    long_description=readfile('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
    ],
    install_requires=[
        'requests',
        'numpy',
        'pandas',
        'matplotlib',
        'jupyter',
        'python-Levenshtein',
    ],
)
