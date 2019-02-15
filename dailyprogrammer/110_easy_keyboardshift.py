#/usr/bin/env python2

# Challenge #110 [easy] Keyboard Shift

shifted = { 'w':'q', 'e':'w', 'r':'e', 't':'r', 'y':'t', 'u':'y', 'i':'u',
            'o':'i', 'p':'o', '[':'p', '{':'p', 's':'a', 'd':'s', 'f':'d', 
            'g':'f', 'h':'g', 'j':'h', 'k':'j', 'l':'k', ';':'l', ':':'l',
            'x':'z', 'c':'x', 'v':'c', 'b':'v', 'n':'b', 'm':'n', ',':'m', 
            '<':'m', ' ':' ' }

input1 = "Jr;;p ept;f"
input2 = "Lmiyj od ,u jrtp"

def shift(input, conversion):
    """ Accept input string and conversion dict, return corrected string """
    result = ''
    for character in input:
        if character.isupper():
            result += conversion[character.lower()].upper()
        else:
            result += conversion[character]
    return result


if __name__ == '__main__':

    print shift(input1, shifted)
    print shift(input2, shifted)
