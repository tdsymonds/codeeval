import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            # find the last space and trim
            last_space = line[::-1].find(' ')
            line = line[:-last_space-1]
            # find the next last space and trim
            # if needed.
            last_space = line[::-1].find(' ')
            if last_space == -1:
                print line
            else:
                print line[-last_space:]