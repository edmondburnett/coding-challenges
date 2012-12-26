#!/usr/bin/env python2

# Challenge #76 [easy] Title case

phrase = "the quick brown fox jumps over the lazy dog"
exceptions = ['jumps', 'the', 'over']


def titlecase(phrase, exceptions):
    """
    Accept a string and list of exceptions, then output a title-cased result.
    """
    phrase_list = phrase.split()
    for i in range(len(phrase_list)):
        if phrase_list[i] not in exceptions or i == 0:
            print(phrase_list[i].capitalize()),
        else: 
            print(phrase_list[i].lower()),
        if i == phrase_list[-1]: print " "


titlecase(phrase, exceptions)
