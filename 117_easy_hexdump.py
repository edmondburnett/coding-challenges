# Challenge #117 [easy] Hexdump to ASCII
# http://redd.it/16jiuq

def hexconvert(filename):
    """ Accept a filename and return a hex list of it's characters """
    hexlist = []
    file = open(filename, 'r')
    while file:
        try:
            hexlist.append(hex(ord(file.read(1)))[2:])
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
    newlist = []
    for line in range(len(linenumbers)):
        #newlist.append(linenumbers[line])
        hexstring = str(linemumbers[line])
        hexend = (line+1)*16
        for char in bytelist[line*16:hexend]:
            #newlist.append(char)
            hexstring = hexstring + ' ' + char
        # currentline = bytelist[x*16:hexend]
        # end = []
        # currentline = []
        # currentline = bytelist[begin*16:end]
        # hexbegin += 1
    return hexstring

# for n in linenumbers, concatinate a string of 16 hex bytes

#for charcount,char in enumerate(hexlist):
#    if (charcount % 16) == 0:
#        linecount += 1
#        hexend = linecount * 16
#        currentline = []
#        currentline = hexlist[hexbegin*16:hexend]
#        hexbegin += 1
#        print hex(linecount)[2:], currentline

hexchars = hexconvert('README.md')
print hexchars
print
stuff = linecounter(hexchars)
print stuff
print
print hexlines(stuff, hexchars)
