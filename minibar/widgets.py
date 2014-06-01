# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from minibar.formatter import Formatter


class Widget(object):
    def __init__(self, counter, total, elapsed):
        self.counter = counter
        self.total = total
        self.elapsed = elapsed


class Bar(Widget):
    name = 'bar'
    template = '{red}[{green}{bar:{bar_width}}{red}]{reset}'
    filler = '▏▎▍▌▋▊▉'

    def __format__(self, width):
        if not width:
            width = 50

        bar_width = int(width) - 2
        tmp = (((self.counter * 100.0) / self.total) * bar_width) / 100
        bar = self.filler[-1] * int(tmp)
        rest = tmp % 1
        if rest:
            bar += self.filler[int((tmp % 1) * len(self.filler))]

        return Formatter().format(self.template, bar=bar, bar_width=bar_width)


class Total(Widget):
    name = 'total'

    def __format__(self, format_spec):
        return format(self.total, format_spec)


class Counter(Widget):
    name = 'i'

    def __format__(self, format_spec):
        return format(self.counter, format_spec)


class Elapsed(Widget):
    name = 'elapsed'

    def __format__(self, format_spec):
        if not format_spec:
            format_spec = '.0f'
        return format(self.elapsed, format_spec)


class ETA(Widget):
    name = 'eta'

    def __format__(self, format_spec):
        eta = int((self.elapsed * (self.total - self.counter)) // self.counter)
        if eta < 60:
            unit = 's'
        elif 60 <= eta < 3600:
            unit = 'm'
            eta = eta // 60
        else:
            unit = 'h'
            eta = eta // 3600

        return format(str(eta) + unit, format_spec)
