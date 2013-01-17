# Challenge #117 [easy] Hexdump to ASCII
# http://redd.it/16jiuq

def hexconvert(filename):
    """ Accept a filename and return a list of hex bytes """
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

#for charcount,char in enumerate(hexlist):
#    if (charcount % 16) == 0:
#        linecount += 1
#        hexend = linecount * 16
#        currentline = []
#        currentline = hexlist[hexbegin*16:hexend]
#        hexbegin += 1
#        print hex(linecount)[2:], currentline

print linecounter(hexconvert('117_easy_hexdump.py'))
