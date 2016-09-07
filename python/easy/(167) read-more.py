import sys

with open(sys.argv[1], 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line:
            line = line.strip()
            if len(line) <= 55:
                print line
            else:
                line = line[:40]
                last_space = line[::-1].find(' ')
                if last_space >= 0:
                    print '%s%s' % (line[:-last_space-1], '... <Read More>')
                else:
                    print '%s%s' % (line, '... <Read More>')
