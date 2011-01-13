#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

import message

classifiers = [i for i in '''
Development Status :: 3 - Alpha
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development
Topic :: Software Development :: Libraries
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Utilities
'''.split('\n') if i.strip()]
#print classifiers
	
setup(
	name = 'message',
	version = message.__version__,

	packages = find_packages(),

	description = 'A message-oriented programming library for python.',
	long_description = 'See http://code.google.com/p/python-message for documentation.',
	author = message.__author__,
	author_email = 'mail@laiyonghao.com',

	license = 'MIT',
	keywords = ('message-oriented', 'signal-slot', 'publish-subscribe'),
	platforms = 'Independant',
	url = 'http://code.google.com/p/python-message/',
	classifiers = classifiers
)

