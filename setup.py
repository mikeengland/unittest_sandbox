# coding: utf8

from setuptools import setup
import os
from unittest_sandbox import __version__


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='unittest_sandbox',
    version=__version__,

    author='Michael England',

    # License
    license='Apache License Version 2.0',

    packages=['unittest_sandbox'],

    # Details
    url='https://github.com/mikeengland/unittest_sandbox',

    description='unittest_sandbox provides a @sandbox decorator which ensures unit test methods do not '
                'make any socket/web requests during test execution.',
    long_description=readme(),

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ],
    keywords='unittest unittests testcase sandbox internet block decorator socket requests urllib',

    test_suite='unittest_sandbox.tests',
)
