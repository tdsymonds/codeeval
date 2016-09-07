import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            # cast to a set to remove duplicates and map
            # to int to sort
            sorted_int_list = sorted(map(int, set(line.split(','))))
            # map back to string to join and print
            print ','.join(map(str, sorted_int_list))
        