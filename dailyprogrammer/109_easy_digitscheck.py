#!/usr/bin/env python2

# Challenge #109 [easy] Digits Check

def checkdigit(x):
    """ Check if input string is a digit """
    if x.isdigit(): return True
    else: return False

print "123: ", checkdigit("123")
print "ABC: ", checkdigit("ABC")
