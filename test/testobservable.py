# -*- coding:utf-8 -*-
# vim: ts=4 sw=4 sts=4 et:

from message import observable


def greet(people):
    print('hello, %s.' % people.name)


@observable
class Foo(object):
    def __init__(self, name):
        print('Foo')
        self.name = name

        self.sub('greet', greet)

    def pub_greet(self):
        self.pub('greet', self)


@observable
class Bar(object):
    def __init__(self, name):
        print('Bar')
        self.name = name

    def sub_greet(self, func):
        self.sub('greet', func)

    def pub_greet(self):
        self.pub('greet', self)


foo = Foo('lai')
foo.pub_greet()
