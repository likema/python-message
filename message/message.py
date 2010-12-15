#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weakref import ref

__all__ = [
		'sub',
		'unsub',
		'pub',
		'declare',
		'retract',
		]

from collections import defaultdict as dd
from collections import Hashable

_router = dd(set)

_board = {}

def sub(msg, func):
	assert isinstance(msg, Hashable)
	assert callable(func)
	global _router
	_router[msg].add(ref(func))
	if msg in _board:
		a, kw = _board[msg]
		func(*a, **kw)

def unsub(msg, func):
	assert isinstance(msg, Hashable)
	assert callable(func)
	global _router
	if msg not in _router:
		return
	try:
		_router[msg].remove(ref(func))
	except KeyError:
		pass
	
def pub(msg, *a, **kw):
	assert isinstance(msg, Hashable)
	global _router
	if msg not in _router:
		return
	removed = []
	for fref in _router[msg]:
		func = fref()
		if func:
			func(*a, **kw)
		else:
			removed.append(fref)
	for i in removed:
		_router[msg].remove(i)

def declare(msg, *a, **kw):
	assert isinstance(msg, Hashable)
	global _board
	_board[msg] = (a, kw)
	return pub(msg, *a, **kw)

def retract(msg):
	assert isinstance(msg, Hashable)
	global _board
	try:
		_board.pop(msg)
	except KeyError:
		pass

if __name__ == '__main__':
	def greet(name):
		print 'hello, %s.'%name
	
	sub('greet', greet)
	pub('greet', 'lai')
	pub('greet', 'smallfish')
	pub('greet', 'guido')
	unsub('greet', greet)
	pub('greet', 'world')
	print '*' * 30
	sub('greet', greet)
	declare('greet', 'world')
	
	def greet2(name):
		print 'hello, %s. greet2'%name
	
	sub('greet', greet2)

	pub('greet', 'spring')
	
	retract('greet')

	def greet3(name):
		print 'hello, %s. greet3'%name
	
	sub('greet', greet3)
#	pub('greet', 'lv')

