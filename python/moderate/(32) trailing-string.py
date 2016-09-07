import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            split_line = line.split(',')

            first_string = split_line[0]
            second_string = split_line[1]

            length_of_second_string = len(second_string)

            if first_string[::-1][:length_of_second_string] == second_string[::-1]:
                print 1
            else:
                print 0
