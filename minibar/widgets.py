# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from minibar.formatter import Formatter


class Widget(object):
    def __init__(self, counter, total):
        self.counter = counter
        self.total = total


class Bar(Widget):
    name = 'bar'
    template = '{red}[{green}{bar:{bar_width}}{red}]{reset}'
    filler = '▏▎▍▌▋▊▉'

    def __format__(self, width):
        bar_width = int(width) - 2
        tmp = (((self.counter * 100.0) / self.total) * bar_width) / 100
        bar = self.filler[-1] * int(tmp)
        rest = tmp % 1
        if rest:
            bar += self.filler[int((tmp % 1) * len(self.filler))]

        return Formatter().format(self.template, bar=bar, bar_width=bar_width)


class Total(Widget):
    name = 'total'

    def __format__(self, width):
        return u'{}'.format(self.total)


class Counter(Widget):
    name = 'i'

    def __format__(self, width):
        return u'{}'.format(self.counter)
