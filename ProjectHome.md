A message-oriented programming library for python.
<a href='Hidden comment: 
= Overview =
<wiki:gadget url="https://python-message.googlecode.com/svn/trunk/doc/python-message-0.1.0-slide-gadget.xml" width="700" height="360" border="0" />
'></a>
# Install #
run command
```
easy_install -U message
```
# Sample #
  * code
```
import message
def hello(name):
  print 'hello, %s.'%name
message.sub('greet', hello)
message.pub('greet', 'lai')
```
  * output
```
hello, lai.
```
# User Guide #
  * [中文](http://blog.csdn.net/lanphaday/article/details/7215315)
  * [English](http://code.google.com/p/python-message/wiki/UserGuide)