import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            
            split_line = line.split(';')

            list1 = split_line[0].split(',')
            list2 = split_line[1].split(',')
            set_intersection = set(list1).intersection(list2)

            # convert to int, sort and then back to string to join
            print ','.join(map(str, sorted(map(int, set_intersection))))