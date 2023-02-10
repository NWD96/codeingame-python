import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()

for i in range(h):
    mot = ""
    row = input()
    for j in t.upper():
        if j >= 'A' and j <= 'Z':
            lettre = ord(j) - ord('A')
            mot += str(row[(lettre*l):(lettre+1)*l])
        else:
            mot += str(row[104:108])
    print(mot)
