import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            print str(bin(int(line)))[2:].count('1')
