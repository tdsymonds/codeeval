import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            for word in line.split(' '):
                new_word = word[0].upper() + word[1:]
                print new_word, 
            print