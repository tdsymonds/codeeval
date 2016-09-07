import sys

with open(sys.argv[1], 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line:
            line = line.strip().split(',')
            n = int(line[0])
            m = int(line[1])
            print n-((n//m)*m)