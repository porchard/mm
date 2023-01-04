#!/usr/bin/env python

import re
from setuptools import setup, find_packages

with open("mm/__init__.py") as f:
    __version__ = re.search(r'__version__ ?= ?[\'\"]([\w.]+)[\'\"]', f.read()).group(1)

# Setup information
setup(
    name = 'mm',
    version = __version__,
    packages = find_packages(),
    description = 'Utility functions for manipulating single-nucleus market matrix files.',
    author = 'Peter Orchard',
    author_email = 'porchard@umich.edu',
    scripts = ['bin/mm'],
    install_requires = [
        'pandas', 'numpy']
)
