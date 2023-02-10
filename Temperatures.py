import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temp = 5526

if n != 0:
    for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        if abs(temp) > abs(t):
            temp = t
        elif abs(temp) == abs(t):
            temp = max(t, temp)

    print(temp)

elif n == 0:
    print(0)
