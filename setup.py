#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import newsletter2go

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = newsletter2go.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-newsletter2go',
    version=version,
    description="""An email backend for Django that uses Newsletter2Go transactional emails""",
    long_description=readme + '\n\n' + history,
    author='Lukas Klein',
    author_email='lukas@productgang.com',
    url='https://github.com/productgang/django-newsletter2go',
    packages=[
        'newsletter2go',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-newsletter2go',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
