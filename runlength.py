#!/usr/bin/python2

# Challenge #86: Run-length encoding

import re

thestring = "Heeeeelllllooooo nurse!"

def runlength(s):
    array = [(0, s[0])]
    for x in range(len(s)):
        if s[x] in array[-1]:
            array[-1] = (array[-1][0]+1, array[-1][1])
        else:
            array.append((1, s[x]))
    print array


def encode(text):
    pairs = []
    current = None
    run = 0
    for v in text:
        if current is None: 
            current=v
        if v != current:
            pairs.append((run,current))
            run = 1
            current = v
        else: run += 1
    pairs.append((run, current))
    return pairs



if __name__ == "__main__":
#    runlength(thestring)
#    print x.group(0)
    print encode(thestring)
