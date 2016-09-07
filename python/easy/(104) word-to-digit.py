import sys

numbers_in_words = ['zero', 'one', 'two', 'three', 'four', 
    'five', 'six', 'seven', 'eight', 'nine']

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            num_string = ''
            for num in line.split(';'):
                num_string += str(numbers_in_words.index(num))
            print num_string
