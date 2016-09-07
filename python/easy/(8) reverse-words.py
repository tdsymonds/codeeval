import sys

with open(sys.argv[1], 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line:
            print ' '.join(list(reversed(line.split())))
            