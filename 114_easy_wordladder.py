#!/usr/bin/env python2

# Challenge #114 [easy] Word Ladder Steps

word_list = open('fourletterwords.txt', 'r').read().splitlines()

def ladder(word):
    """ 
    Accept a 4-letter word and return list of words that match 
    exactly 3 of it's characters.
    """
    ladder_list = []
    for w in word_list:
        num = 0
        for letter in range(4):
            if w[letter] == word[letter]:
                num += 1
        if num == 3:
            ladder_list.append(w)
    return ladder_list


if __name__ == '__main__':
    result = ladder("best")
    for x in range(len(result)):
        print result[x]
