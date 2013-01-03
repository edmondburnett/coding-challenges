#!/usr/bin/env python2

# Challenge #70 [easy] Most common words in a file

def wordcount(filename):
    """ Accept a filename and paramater n, return n most common words """
    wordlist = open(filename, 'r').read().split()

    results = {}
    for x in wordlist:
        if x in results:
            count = results[x] + 1
            results.update({x : count})
        else:
            results[x] = 1

    return results


def printwords(list, n):
    count = 0
    for key,value in newlist:
        if count < n:
            print key,value
            count += 1
        else:
            break


newlist = sorted(wordcount('loremipsum.txt', 10).iteritems(), \
        key=lambda item: -item[1])

count = 0
for key,value in newlist:
    if count < 10:
        print key,value
        count += 1
    else:
        break
