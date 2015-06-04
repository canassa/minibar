# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
import sys
import os
import string
import time

from minibar.widgets import Widget
from minibar.formatter import Formatter

__version__ = '0.4.0'
__all__ = ['bar', 'Minibar']


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY2:
    text_type = unicode
else:
    text_type = str


def get_terminal_width():
    stty_size = os.popen('stty size', 'r').read()

    if not stty_size:
        # Terminal might not be available, fallback to 80 columns
        return 80
    else:
        rows, columns = stty_size.split()
        return int(columns)


def iprint(string, out=sys.stdout):
    """ prints string and writes to tty-enabled device

    output device is a file-like object and must implement isatty()
    """
    if out.isatty():
        print('\r' + string, file=out, end='')
        out.flush()


def bar(iterator, template='{i}/{total} {bar:fill}', total=None, out=sys.stdout):
    """ Shows a progress bar for the given iterator, yields the iterator object
        This makes the usage of the progress bar transparent for the code using the iterator

        iterator: an iterable object
        template: a custom format for the minibar, see widgets for all available fields
        total   : the number minibar should use as total value to count up to
                  - default is len(iterator)
        out     : a file-like object to write the minibar to, can be set to sys.stderr
                  if you need stdout for your program - default is sys.stdout
        """

    if total is None:
        total = len(iterator)

    minibar = Minibar(total, template, out)
    for value in minibar.iter(iterator):
        yield value


class Minibar(object):
    def __init__(self, total, template='{i}/{total} {bar:fill}', out=sys.stdout):
        self.total = total
        self.template = text_type(template)
        self.enabled_widgets = list(self._get_widgets())
        self.terminal_width = get_terminal_width()
        self.fmt = Formatter(self.terminal_width)
        self.start_time = time.time()
        self.counter = 1
        self.out=out
        self.render()

    def _get_widgets(self):
#         this doesn't work on 2.6 :-(
#         avaliable_widgets = {w.name: w for w in Widget.__subclasses__()}
        avaliable_widgets = dict([(w.name, w) for w in Widget.__subclasses__()])
        for _, field_name, _, _ in string.Formatter().parse(self.template):
            if field_name in avaliable_widgets:
                yield avaliable_widgets[field_name]

    def iter(self, iterator):
        for value in iterator:
            self.render()
            self.counter += 1
            yield value

    def render(self):
        if self.counter <= self.total:
            elapsed = time.time() - self.start_time
#             this doesn't work on 2.6 :-(
#             kwargs = {w.name: w(self.counter, self.total, elapsed) for w in self.enabled_widgets}
            kwargs = dict([(w.name, w(self.counter, self.total, elapsed)) for w in self.enabled_widgets])
            iprint(self.fmt.format(self.template, **kwargs),self.out)

    def inc(self, increment=1):
        self.render()
        self.counter += increment
