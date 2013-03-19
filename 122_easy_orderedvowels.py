# Challenge #122 [easy] Words with Ordered Vowels
# http://redd.it/1aih0v


def ordered_vowels(filename):
    """ Input a text file containing one word on each line.
        Return a list of the words which contain all vowels in
        alphabetical order, non-repeated. """
    wordlist = open(filename, 'r').read().splitlines()
    vowels   = ['a', 'e', 'i', 'o', 'u']
    result   = []

    for word_pos in range(len(wordlist)):
        current = []
        for letter in wordlist[word_pos]:
            if letter.lower() in vowels:
                current.append(letter.lower())
        if current == vowels:
            result.append(wordlist[word_pos])

    return result


for word in ordered_vowels('enable1.txt'):
    print word
