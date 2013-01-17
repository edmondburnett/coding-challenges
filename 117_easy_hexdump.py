# Challenge #117 [easy] Hexdump to ASCII
# http://redd.it/16jiuq

def hexconvert(filename):
    """ Accept a filename and return a hex list of it's characters """
    hexlist = []
    file = open(filename, 'r')
    while file:
        try:
            stuff = hex(ord(file.read(1)))[2:]
            if len(stuff) == 1:
                stuff = '0' + stuff
            #hexlist.append(hex(ord(file.read(1)))[2:])
            hexlist.append(stuff)
        except TypeError:
            break
    return hexlist


def linecounter(bytelist):
    """ Return a list of formatted line numbers """
    linecount = 0
    result = []
    for charcount, char in enumerate(bytelist):
        if (charcount % 16) == 0:
            linecount += 1
            result.append(hex(linecount)[2:])
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
    hexchars = hexconvert('README.md')
    stuff = linecounter(hexchars)

    for x in hexlines(stuff, hexchars):
        print x
