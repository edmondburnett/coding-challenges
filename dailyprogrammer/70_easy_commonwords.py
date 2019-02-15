#!/usr/bin/env python2

# Challenge #70 [easy] Most common words in a file

def wordcount(filename):
    """ Accept a filename, return dict of words and their occurance count """
    wordlist = open(filename, 'r').read().split()

    results = {}
    for x in wordlist:
        if x in results:
            count = results[x] + 1
            results.update({x : count})
        else:
            results[x] = 1

    return results


def topwords(filename, n):
    """ Build a sorted list from wordcount() and print n most used words """
    sorted_list = sorted(wordcount(filename).iteritems(), key=lambda item: -item[1])
    count = 0
    for key,value in sorted_list:
        if count < n:
            print key,value
            count += 1
        else:
            break


topwords('loremipsum.txt', 10)
