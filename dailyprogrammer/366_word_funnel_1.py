#!/usr/bin/env python



if __name__ == '__main__':
    with open('enable1.txt') as words:
        for word in words:
            word = word.strip()
            print(word)