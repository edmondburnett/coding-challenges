# Challenge #117 [easy] Hexdump to ASCII
# http://redd.it/16jiuq

file = open('loremipsum.txt', 'r')
hexlist = []
linecount = 0

while file:
    try:
        hexlist.append(hex(ord(file.read(1)))[2:].upper())
    except TypeError:
        break

for charcount,x in enumerate(hexlist):
    if (charcount % 16) == 0:
        linecount += 1
        #print linecount, hexlist[:16]

# for every 16 items in hexlist, print linecount and items
