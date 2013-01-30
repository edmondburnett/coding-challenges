# Challenge #119 [easy] Change Calculator
# http://redd.it/17f3y2

import sys
from decimal import *

def change(money):
    """
    Accept a value, round to the nearest penny, and output the minimum # of
    coins which equal that amount of money.
    """
    getcontext().rounding = ROUND_HALF_UP
    value = int(Decimal(money).quantize(Decimal('0.01')) * 100)
    print "Quarters: ",
    if value >= 25:
        print value/25
        value %= 25
    else: print 0
    print "Dimes: ",
    if value >= 10:
        print value/10
        value %= 10
    else: print 0
    print "Nickles: ",
    if value >= 5:
        print value/5
        value %= 5
    else: print 0
    print "Pennies: ",
    if value >= 1:
        print value/1
    else: print 0


if __name__ == '__main__':
    try:
        input = sys.argv[1]
    except IndexError:
        print "No input specified."
        print "Usage: python 119_changecalc.py <dollar amount>"
        sys.exit()

    change(input)
