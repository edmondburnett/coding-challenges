#!/usr/bin/env python2

# Challenge #115 [easy] Guess-that-number game
# http://redd.it/15ul7q

from random import randrange

def guessing(answer):
    """ Accept an int and prompt user to guess it correctly """
    print "C> Welcome to guess-that-numbers game!"
    print "C> I have already picked a number in [1, 100]. Please make a guess."
    print "C> Type \"exit\" to quit."

    guesses = 0
    while True:
        try:
            response = raw_input("U> ")
            guesses += 1
            if response == "exit":
                print "C> Exiting."
                break
            elif int(response) == answer:
                print "C> Correct! That is my number, you won in "\
                        + str(guesses) + " attempts."
                break
            elif int(response) < answer:
                print "C> Wrong. That number is below my number."
            elif int(response) > answer:
                print "C> Wrong. That number is above my number."

        except ValueError:
            print "C> Invalid input."


guessing(randrange(1,100))
