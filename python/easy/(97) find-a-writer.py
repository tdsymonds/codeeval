import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            parts = line.split('| ')
            text = parts[0]
            key = parts[1].split(' ')
            author = ''
            for number in key:
                author += text[int(number)-1]
            print author