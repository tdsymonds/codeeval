import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        print line.lower()