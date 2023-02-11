import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
x1 = y1  = 0
x2, y2 = w - 1, h - 1 


while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if 'U' in bomb_dir:
        y2 = y0 - 1
    elif 'D' in bomb_dir:
        y1 = y0 + 1
    if 'L' in bomb_dir:
        x2 = x0 - 1
    elif 'R' in bomb_dir:
        x1 =x0 + 1
    x0 = x1 + math.ceil((x2  - x1)/2)
    y0 = y1 + math.ceil((y2  - y1)/2)
    # the location of the next window Batman should jump to.
    print(x0, y0)
