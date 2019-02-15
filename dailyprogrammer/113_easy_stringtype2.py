#!/usr/bin/env python2

# Challenge #113 [easy] String-type checking
# variant/solution #2

import re

# sample input data
strings = ['99.9', '9-16-1983', '11', '42.0', '06-23-1999', 'bluesteel techology', '9115']

# regular expression patterns
float_pattern = "\d\.\d"
date_pattern  = "\d*\-\d*\-\d\d*"
int_pattern   = "\d+$"
text_pattern  = ".*"


def bluesteel(num):
    """ Search data and return resulting 'type' of string """
    if re.search(float_pattern, strings[num]):
        result = "float"
    elif re.search(date_pattern, strings[num]):
        result = "date"
    elif re.search(int_pattern, strings[num]):
        result = "int"
    elif re.search(text_pattern, strings[num]):
        result = "text"
    else:
        result = "Unknown type or data empty."

    return result


if __name__ == '__main__':
    for x in range(len(strings)):
        print bluesteel(x)
