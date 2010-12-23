#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.insert(0, '..')

from message import observable

def greet(context, people):
	print 'hello, %s.'%people.name

@observable
class Foo(object):
	def __init__(self, name):
		self.name = name

	def sub_greet(self, func):
		self.sub('greet', func)
	
	def pub_greet(self):
		self.pub('greet', self)

foo = Foo('lai')
#foo.sub('greet', greet)
#foo.pub('greet', foo)
foo.sub_greet(greet)
foo.pub_greet()

print '*' * 30
bar = Foo('yong')

bar.sub('greet', greet)
bar.pub('greet', bar)


