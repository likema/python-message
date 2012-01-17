#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.insert(0, '..')

from message import observable

def greet(people):
	print 'hello, %s.'%people.name

@observable
class Foo(object):
	def __init__(self, name):
		print 'Foo'
		self.name = name

#	def sub_greet(self, func):
#		self.sub('greet', func)
		self.sub('greet', greet)
	
	def pub_greet(self):
		self.pub('greet', self)

@observable
class Bar(object):
	def __init__(self, name):
		print 'Bar'
		self.name = name

	def sub_greet(self, func):
		self.sub('greet', func)
	
	def pub_greet(self):
		self.pub('greet', self)

foo = Foo('lai')
#foo.sub('greet', greet)
#foo.pub('greet', foo)
#foo.sub_greet(greet)
foo.pub_greet()

# print '*' * 30
# bar = Foo('yong')
# 
# bar.sub('greet', greet)
# bar.pub('greet', bar)
# 
bar = Bar('hao')
bar.sub('greet', greet)
bar.pub('greet', bar)
 

