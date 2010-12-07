#!/usr/bin/env python
# -*- coding:utf-8 -*-

__all__ = [
		'sub',
		'unsub',
		'pub',
		]

from collections import defaultdict as dd
from collections import Hashable

_pump = dd(set)

def sub(msg, func):
	assert isinstance(msg, Hashable)
	assert callable(func)
	global _pump
	_pump[msg].add(func)

def unsub(msg, func):
	assert isinstance(msg, Hashable)
	assert callable(func)
	global _pump
	if msg not in _pump:
		return
	try:
		_pump[msg].remove(func)
	except KeyError:
		pass
	
def pub(msg, *a, **kw):
	assert isinstance(msg, Hashable)
	global _pump
	if msg not in _pump:
		return
	for func in _pump[msg]:
		func(*a, **kw)

if __name__ == '__main__':
	def greet(name):
		print 'hello, %s.'%name
	
	sub('greet', greet)
	pub('greet', 'lai')
	pub('greet', 'smallfish')
	pub('greet', 'guido')
	unsub('greet', greet)
	pub('greet', 'world')

