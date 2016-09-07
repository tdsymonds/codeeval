import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        line_list = line.split(', ')
        sentance = line_list[0]
        chars_to_remove = line_list[1]

        for char in chars_to_remove:
            sentance = sentance.replace(char, '')

        print sentance
