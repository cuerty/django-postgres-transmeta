#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import postgres_transmeta

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = postgres_transmeta.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='postgres_transmeta',
    version=version,
    description="""Django translation for model content similar to django-transmeta but using PostgreSQL's hstore.""",
    long_description=readme + '\n\n' + history,
    author='Angel Freire',
    author_email='cuerty@gmail.com',
    url='https://github.com/cuerty/django-postgres-transmeta',
    packages=[
        'postgres_transmeta',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="GNU Lesser General Public License (LGPL), Version 3",
    zip_safe=False,
    keywords='django-postgres-transmeta',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
