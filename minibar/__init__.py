# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
import sys
import os
import string
import time

from minibar.widgets import Widget
from minibar.formatter import Formatter

__version__ = '0.2.3'
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


def iprint(string):
    if sys.stdout.isatty():
        print('\r' + string, file=sys.stdout, end='')
        sys.stdout.flush()


def bar(iterator, template='{i}/{total} {bar:fill}', total=None):
    if total is None:
        total = len(iterator)

    minibar = Minibar(total, template)
    for value in minibar.iter(iterator):
        yield value


class Minibar(object):
    def __init__(self, total, template='{i}/{total} {bar:fill}'):
        self.total = total
        self.template = text_type(template)
        self.enabled_widgets = list(self._get_widgets())
        self.terminal_width = get_terminal_width()
        self.fmt = Formatter(self.terminal_width)
        self.start_time = time.time()
        self.counter = 1
        self.render()

    def _get_widgets(self):
        avaliable_widgets = {w.name: w for w in Widget.__subclasses__()}
        for _, field_name, _, _ in string.Formatter().parse(self.template):
            if field_name in avaliable_widgets:
                yield avaliable_widgets[field_name]

    def iter(self, iterator):
        for value in iterator:
            self.render()
            self.counter += 1
            yield value

    def render(self):
        elapsed = time.time() - self.start_time
        kwargs = {w.name: w(self.counter, self.total, elapsed) for w in self.enabled_widgets}
        iprint(self.fmt.format(self.template, **kwargs))

    def inc(self, increment=1):
        self.render()
        self.counter += increment
