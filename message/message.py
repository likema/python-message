#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weakref import ref
from copy import copy

from collections import defaultdict as dd
from collections import Hashable

__all__ = [
		'sub',
		'unsub',
		'pub',
		'declare',
		'retract',
		'get_declarations',
		]

_broker = dd(set)
_board = {}

def sub(msg, func):
	assert isinstance(msg, Hashable)
	assert callable(func)
	global _broker
	_broker[msg].add(ref(func))
	if msg in _board:
		a, kw = _board[msg]
		func(*a, **kw)

def unsub(msg, func):
	assert isinstance(msg, Hashable)
	assert callable(func)
	global _broker
	if msg not in _broker:
		return
	try:
		_broker[msg].remove(ref(func))
	except KeyError:
		pass
	
def pub(msg, *a, **kw):
	assert isinstance(msg, Hashable)
	global _broker
	if msg not in _broker:
		return
	removed = []
	for fref in copy(_broker[msg]):
		func = fref()
		if func:
			func(*a, **kw)
		else:
			removed.append(fref)
	for i in removed:
		try:
			_broker[msg].remove(i)
		except KeyError:
			pass

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

def get_declarations():
	return _board.keys()

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
	assert get_declarations()
	
	def greet2(name):
		print 'hello, %s. greet2'%name
	
	sub('greet', greet2)

	pub('greet', 'spring')

	
	retract('greet')

	def greet3(name):
		print 'hello, %s. greet3'%name
	
	sub('greet', greet3)

	print '*' * 30
	def greet4(name):
		print 'hello, %s. greet4'%name
		unsub('greet', greet4)
	sub('greet', greet4)
	pub('greet', 'lv')
	pub('greet', 'ma')

