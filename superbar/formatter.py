# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import string


class Formatter(string.Formatter):
    COLORS = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }

    def __init__(self, width=None):
        self.width = width

    def vformat(self, format_string, args, kwargs, recur=False, width=None):
        result = []
        for literal_text, field_name, format_spec, conversion in self.parse(format_string):
            # output the literal text
            if literal_text:
                result.append(literal_text)

            if format_spec == 'fill':
                recur = True
                result.append('{' + field_name + '}')
                continue

            # if there's a field, output it
            if field_name is not None:
                obj, _ = self.get_field(field_name, args, kwargs)

                # do any conversion on the resulting object
                obj = self.convert_field(obj, conversion)

                # expand the format spec, if needed
                format_spec = self.vformat(format_spec, args, kwargs)

                # format the object and append to the result
                if width is None:
                    field_result = format(obj, format_spec)
                else:
                    field_result = format(obj, str(width))

                result.append(field_result)

        result = ''.join(result)

        if recur:
            return self.vformat(result, args, kwargs, width=self.width - len(result))

        return result

    def get_value(self, key, args, kwargs):
        if isinstance(key, int):
            return args[key]
        elif key in kwargs:
            return kwargs[key]
        elif key in self.COLORS:
            return self.COLORS[key]
        else:
            return '{' + key + '}'
