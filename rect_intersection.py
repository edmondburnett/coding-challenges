#!/usr/bin/env python2

# Challenge #87: Rectangle Intersection

rect1 = [3, 3, 10, 10]
rect2 = [6, 6, 12, 12]

intersect = [max(rect1[0],rect2[0]), 
             max(rect1[1],rect2[1]),
             min(rect1[2],rect2[2]),
             min(rect1[3],rect2[3])]

print intersect
