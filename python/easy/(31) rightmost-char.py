import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            line = line.split(',')
            
            s = line[0]
            t = line[1]

            index = s[::-1].find(t)

            if index >= 0:
                print len(s)-index-1
            else:
                print index
