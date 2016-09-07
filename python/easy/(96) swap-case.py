import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            sentance = ''
            for char in line:
                if char.islower():
                    sentance += char.upper()
                else:
                    sentance += char.lower()
            print sentance
