import math
import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            # split and retrieve x1, y1, x2, y2
            line = line.split(') (')
            coordinate1 = line[0][1:].split(', ')
            coordinate2 = line[1][:-1].split(', ')
            x1 = int(coordinate1[0])
            y1 = int(coordinate1[1])
            x2 = int(coordinate2[0])
            y2 = int(coordinate2[1])
            print int(math.sqrt((x1-x2)**2+(y1-y2)**2))
