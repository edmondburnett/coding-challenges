# Challenge #117 [easy] Hexdump to ASCII
# http://redd.it/16jiuq

file = open('117_easy_hexdump.py', 'r')
hexlist = []
linecount = 0
hexcount  = 0
hexbegin = 0

while file:
    try:
        hexlist.append(hex(ord(file.read(1)))[2:])
    except TypeError:
        break

for charcount,char in enumerate(hexlist):
    if (charcount % 16) == 0:
        linecount += 1
        hexend = linecount * 16
        currentline = []
        currentline = hexlist[hexbegin*16:hexend]
        hexbegin += 1
        print hex(linecount)[2:], currentline

#if linecount == 1 or linecount % 16:
#    print hex(linecount)[2:]
