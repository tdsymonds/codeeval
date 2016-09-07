import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            for num in sorted(map(float, line.split(' '))):
                print '{0:.3f}'.format(num), 
            print