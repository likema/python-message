#!/usr/bin/env python
# -*- coding:utf-8 -*-

from glob import glob

from setuptools import setup, find_packages

setup(
	name = 'message',
	version = '0.0.1',

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

