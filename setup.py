# coding: utf8

from setuptools import setup

from unittest_sandbox import __version__

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
                    'make any web requests during test execution.',
        long_description="unittest_sandbox provides a decorator which can be used to prevent unit test methods from "
                         "contacting the internet. Decorating a unittest with @sandbox monkey patches the socket "
                         "module to ensure that no web requests reach the outside world.",

        classifiers=[
            'License :: OSI Approved :: Apache Software License',
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Operating System :: POSIX',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
        ],
        keywords='unittest unittests testcase sandbox internet block decorator socket requests urllib',

        tests_require=[
            'mock'
        ],

        test_suite='unittest_sandbox.tests',
)
