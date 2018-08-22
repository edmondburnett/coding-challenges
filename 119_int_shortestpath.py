# Challenge #119 [intermediate] Find the shortest path
# http://redd.it/17jvoh

from __future__ import print_function
import sys

def grid(size):
    """ Generate a (size x size) grid. We don't actually have to do this.  """
    container = []
    for x in range(size):
        l = list(range(size))
        container.append(l)
    for n in container:
        for item in n:
            print(item, end='')
        print("")

    # use random.choice to generate wall/path objects?


grid(int(sys.argv[1]))
