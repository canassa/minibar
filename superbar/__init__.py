__version__ = '0.1.dev1'

import sys
import os

__all__ = ['bar']

COLORS = {c: '\033[9{0}m'.format(i) for i, c in enumerate(['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])}
COLORS['r'] = '\033[0m'


def get_terminal_width():
    rows, columns = os.popen('stty size', 'r').read().split()
    return columns


def iprint(string):
    print('\r' + str(string).format(**COLORS), file=sys.stdout, end='')
    sys.stdout.flush()


def bar(iterator):
    total = len(iterator)
    # template = '▏▎▍▌▋▊▉█'
    template = '▏▎▍▌▋▊▉'
    for counter, i in enumerate(iterator):
        counter += 1
        output = template[-1] * (counter // len(template))
        output += template[counter % len(template)]
        iprint('{:100}'.format(output))
        yield i
