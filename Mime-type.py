import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
type =[[], []]

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    type[0].append(ext.lower())
    type[1].append(mt)


for i in range(q):
    fname = input()  # One file name per line.
    try:
        nom, extension = fname.rsplit('.', 1)
        extension = extension.lower()

        if extension in type[0]:
            j = type[0].index(extension)
            print(type[1][j])
        else:
            print("UNKNOWN")

    except:
        print("UNKNOWN")
