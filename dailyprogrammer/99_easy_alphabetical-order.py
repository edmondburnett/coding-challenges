#!/usr/bin/env python2

# Challenge #99 [easy] Words with letters in alphabetical order

wordlist = open('enable1.txt', 'r').read().splitlines()

def isordered(words):
    """ Return number of words whose letters are in alphabetical order """
    count = 0
    for word in words:
        if list(word) == sorted(word):
            count += 1
        else: continue
    return count

print isordered(wordlist)
