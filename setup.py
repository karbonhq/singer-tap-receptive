#!/usr/bin/env python

from setuptools import setup

setup(name='tap-receptive',
      version='0.0.1',
      description='Singer.io tap for extracting data from the Receptive API',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_receptive'],
      install_requires=[
        'ratelimit==2.2.1',
        'requests==2.24.0',
        'singer-python==5.9.0'
      ],
      entry_points='''
          [console_scripts]
          tap-receptive=tap_receptive:main
      ''',
      packages=['tap_receptive'],
      package_data = {
          'tap_receptive': ['schemas/*.json'],
      }
)
