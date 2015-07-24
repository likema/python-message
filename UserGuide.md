<a href='Hidden comment: 


#summary One-sentence summary of this page.

= Introduction =

Add your content here.


= Details =

Add your content here.  Format your content with:
* Text in *bold* or _italic_
* Headings, paragraphs, and lists
* Automatic links to other wiki pages
'></a>

# Install #
run command.
```
easy_install -U message  
```
# Simple Usage #
```
import message  
def hello(name):  
  print 'hello, %s.'%name  
message.sub('greet', hello)  # subscribe  
message.pub('greet', 'lai') # publish  
```
# Unsubscribe #
```
import message  
def hello(name):  
  print 'hello, %s.'%name  
message.sub('greet', hello)  # subscribe  
message.pub('greet', 'lai') # publish  

message.unsub('greet', hello)  # unsubscribe  
message.pub('greet', 'lai') # publish  
```
or call unsub() in callback.
```
import message  
def hello(name):  
  print 'hello, %s.'%name  
  message.unsub('greet', hello)  
      
message.sub('greet', hello)  
message.pub('greet', 'lai')  
      
message.pub('greet', 'u cann\'t c me.')  
```
# discontinue message dispatch #
```
import message

def hello(name):
  print 'hello %s' % name
  ctx = message.Context()
  ctx.discontinued = True
  return ctx

def hi(name):
  print 'u cann\'t c me.'

message.sub('greet', hello)
message.sub('greet', hi)
message.pub('greet', 'lai')
```
or
```
def hello(name):
  print 'hello %s' % name
  return message.Context(discontinued = True)
```
# observer pattern #
```
from message import observable

def greet(people):
        print 'hello, %s.'%people.name

@observable
class Foo(object):
        def __init__(self, name):
                print 'Foo'
                self.name = name
                self.sub('greet', greet)

        def pub_greet(self):
                self.pub('greet', self)

foo = Foo('lai')
foo.pub_greet()
```
# naming tips #
java/actionscript3 package naming conventions .
```
FOO = 'com.googlecode.python-message.FOO'
```
or use uuid.
```
uuid = 'bd61825688d72b345ce07057b2555719'
FOO = uuid + 'FOO'
```