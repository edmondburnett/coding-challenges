#!/usr/bin/env python2

# Challenge #111 [easy] Star Delete

import re

input = "Stm*xephen Hi*dawking"

def stardelete(string):
    """ Accept a string and return it with *'s and adjacent chars removed. """
    if '*' in string:
        result = re.sub('.\*.', '', string)
    else: result = "String has no '*' characters."
    return result

print stardelete(input)
