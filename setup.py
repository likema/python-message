#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

import message

setup(
	name = 'message',
	version = message.__version__,

	packages = find_packages(),

	description = 'A message-oriented programming library for python.',
	long_description = 'A message-oriented programming library for python.',
	author = 'LaiYonghao',
	author_email = 'mail@laiyonghao.com',

	license = 'MIT',
	keywords = ('message-oriented', 'signal-slots', 'observer pattern'),
	platforms = 'Independant',
	url = 'http://code.google.com/p/python-message/'
)

