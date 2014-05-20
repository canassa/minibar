# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
import sys
import os

__version__ = '0.1.dev1'
__all__ = ['bar']


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY2:
    text_type = unicode
else:
    text_type = str

COLORS = {c: '\033[3{0}m'.format(i) for i, c in enumerate(['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])}
COLORS['r'] = '\033[0m'


def get_terminal_width():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(columns)


def iprint(string, *args):
    print('\r' + text_type(string).format(*args, **COLORS), file=sys.stdout, end='')
    sys.stdout.flush()


def bar(iterator):
    total = len(iterator)
    terminal_width = get_terminal_width() - 2
    template = '▏▎▍▌▋▊▉'
    for counter, i in enumerate(iterator):
        tmp = (((counter * 100.0) / total) * terminal_width) / 100
        output = template[-1] * int(tmp)
        output += template[int((tmp % 1) * len(template))]
        iprint('{red}[{green}{:' + text_type(terminal_width) + '}' + '{red}]{r}', output)

        yield i
