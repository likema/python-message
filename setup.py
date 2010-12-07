from setuptools import setup

## python setup.py bdist_egg

setup(
        name = "message",
        version = "0.0.1",
        author = "LaiYongHao",
        author_email = "mail@laiyonghao.com",
        description = ("message lib"),
        license = "BSD",
        keywords = "python message",
        url = "http://packages.python.org/message",
        packages=['message', 'test', 'doc'],
        )
