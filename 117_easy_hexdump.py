#!/usr/bin/env python2

# Challenge #117 [easy] Hexdump to ASCII
# http://redd.it/16jiuq

import sys, os

def hexconvert(filename):
    """ Accept a filename and return a hex list of it's characters """
    hexlist = []
    file = open(filename, 'r')
    while file:
        try:
            hexbyte = hex(ord(file.read(1)))[2:]
            if len(hexbyte) == 1:
                hexbyte = '0' + hexbyte
            hexlist.append(hexbyte)
        except TypeError:
            break
    return hexlist


def linecounter(bytelist):
    """ Return a list of formatted line numbers """
    linecount = 0
    result = []
    for charcount,char in enumerate(bytelist):
        if (charcount % 16) == 0:
            linecount += 1
            result.append(hex(linecount)[2:].zfill(8))
    return result


def hexlines(linenumbers, bytelist):
    """ Combine line #'s and hex bytes into list of formatted output strings """
    outputlist = []
    for line in range(len(linenumbers)):
        newstring = str(linenumbers[line])
        hexend = (line+1)*16
        for char in (bytelist[line*16:hexend]):
            newstring = newstring + ' ' + char
        outputlist.append(newstring)
    return outputlist


if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        filename = sys.argv[1]
    else:
        print "Input file not specified or doesn't exist."
        sys.exit()

    hexchars = hexconvert(filename)
    linenumbers = linecounter(hexchars)

    for line in hexlines(linenumbers, hexchars):
        print line
