import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            num_list = line.split(' ')
            for i in xrange(len(num_list)):
                popped = num_list.pop()
                if i % 2 is not 1:
                    print popped, 
            print ''
