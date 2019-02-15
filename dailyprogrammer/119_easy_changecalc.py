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
    if value >= 25:
        print "Quarters: ", value/25
        value %= 25
    if value >= 10:
        print "Dimes: ", value/10
        value %= 10
    if value >= 5:
        print "Nickles: ", value/5
        value %= 5
    if value >= 1:
        print "Pennies: ", value/1


if __name__ == '__main__':
    try:
        input = sys.argv[1]
    except IndexError:
        print "No input specified."
        print "Usage: python 119_changecalc.py <dollar amount>"
        sys.exit()

    change(input)
