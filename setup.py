"""
Hello World app for running Python apps on Bluemix
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# To use a consistent encoding
from future import standard_library

standard_library.install_aliases()
from codecs import open
from os import path

# Always prefer setuptools over distutils
from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='stack-search-hack',
    version='1.0.0',
    description='A query based search engine for StackOverflow.',
    long_description=long_description,
    url='https://github.com/sarkar4540/ImprovisedStackSearch',
    license='Apache-2.0'
)
