#!/usr/bin/env python2

# Challenge #113: String-type checking


import re

# sample input data
strings = ['99.9', '9-16-1983', '11', '42.0', '06-23-1999', 'bluesteel techology', '9115']

def bluesteel(pattern, input):
    match = re.search(pattern, input)
    if match:
        return True
    else:
        return False



if __name__ == '__main__':
    for x in range(len(strings)):
        
        # detect float type
        if bluesteel(r'\d+\.\d+', strings[x]):
            print "float"
        
        # detect date type
        elif bluesteel(r'\d+\-\d+\-\d\d+', strings[x]):
            print "date"

        # detect integer type
        elif bluesteel(r'\d+$', strings[x]):
            print "int"
        
        # detect string type (any other data)
        elif bluesteel(r'.+', strings[x]):
            print "text"
        
        # false/empty string
        else:
            print "Error."

