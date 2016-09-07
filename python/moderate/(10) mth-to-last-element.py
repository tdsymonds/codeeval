import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            line_list = line.split(' ')
            index = int(line_list.pop()) - 1
            if index < len(line_list):
                print line_list[::-1][index]
