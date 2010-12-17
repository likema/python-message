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
		'has_declaration',
		]

_broker = dd(list)
_board = {}

class Context(object):
	def __init__(self):
		self.discontinued = False

def sub(topic, func, front = False):
	assert isinstance(topic, Hashable)
	assert callable(func)
	global _broker
	fref = ref(func)
	if fref in _broker[topic]:
		return
	if front:
		_broker[topic].insert(0, fref)
	else:
		_broker[topic].append(fref)
	if topic in _board:
		a, kw = _board[topic]
		func(Context(), *a, **kw)

def unsub(topic, func):
	assert isinstance(topic, Hashable)
	assert callable(func)
	global _broker
	if topic not in _broker:
		return
	try:
		_broker[topic].remove(ref(func))
	except ValueError:
		pass
	
def pub(topic, *a, **kw):
	assert isinstance(topic, Hashable)
	global _broker
	if topic not in _broker:
		return
	removed = []
	context = Context()
	for fref in copy(_broker[topic]):
		func = fref()
		if func:
			func(context, *a, **kw)
		else:
			removed.append(fref)
		if context.discontinued:
			break
	for i in removed:
		try:
			_broker[topic].remove(i)
		except ValueError:
			pass

def declare(topic, *a, **kw):
	assert isinstance(topic, Hashable)
	global _board
	_board[topic] = (a, kw)
	return pub(topic, *a, **kw)

def retract(topic):
	assert isinstance(topic, Hashable)
	global _board
	try:
		_board.pop(topic)
	except KeyError:
		pass

def get_declarations():
	return _board.keys()

def has_declaration(topic):
	assert isinstance(topic, Hashable)
	return topic in _board

if __name__ == '__main__':
	def greet(context, name):
		print 'hello, %s.'%name
	
	sub('greet', greet)
	pub('greet', 'lai')
	pub('greet', 'smallfish')
	pub('greet', 'guido')
	unsub('greet', greet)
	unsub('not existed', greet)
	pub('greet', 'world')
	print '*' * 30
	sub('greet', greet)
	declare('greet', 'world')
	assert get_declarations()
	
	def greet2(context, name):
		print 'hello, %s. greet2'%name
	
	sub('greet', greet2)

	pub('greet', 'spring')
	
	retract('greet')

	def greet3(context, name):
		print 'hello, %s. greet3'%name
	
	sub('greet', greet3)

	print '*' * 30
	def greet4(context, name):
		print 'hello, %s. greet4'%name
		unsub('greet', greet4)
	sub('greet', greet4, front = True)
	pub('greet', 'lv')
	pub('greet', 'ma')

