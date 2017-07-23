# coding: utf8

from setuptools import setup
import os
from unittest_sandbox import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


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
    long_description=read('README.md'),

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
