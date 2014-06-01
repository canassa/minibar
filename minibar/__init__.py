# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
import sys
import os
import string
import time

from minibar.widgets import Widget, Bar
from minibar.formatter import Formatter

__version__ = '0.1'
__all__ = ['bar']


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY2:
    text_type = unicode
else:
    text_type = str


def get_terminal_width():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(columns)


def iprint(string):
    print('\r' + string, file=sys.stdout, end='')
    sys.stdout.flush()


def get_widgets(template, iterator, total):
    avaliable_widgets = {w.name: w for w in Widget.__subclasses__()}
    for _, field_name, _, _ in string.Formatter().parse(template):
       if field_name in avaliable_widgets:
          yield avaliable_widgets[field_name]


def bar(iterator, template='{i}/{total} {bar:fill}', total=None):
    if total is None:
        total = len(iterator)

    enabled_widgets = list(get_widgets(template, iterator, total))
    terminal_width = get_terminal_width()
    fmt = Formatter(terminal_width)
    start_time = time.time()

    for i, value in enumerate(iterator):
        elapsed = time.time() - start_time
        kwargs = {w.name: w(i + 1, total, elapsed) for w in enabled_widgets}
        iprint(fmt.format(template, **kwargs))

        yield value
