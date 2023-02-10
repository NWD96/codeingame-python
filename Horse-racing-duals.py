import sys
import math

table = []
result = []
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    pi = int(input())
    table.append(pi)

table.sort()

for j in range(1, len(table)):
    result.append(int(table[j] - table[j-1]))

result.sort()

print(result[0])
