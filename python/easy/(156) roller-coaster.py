import sys
from string import ascii_lowercase as ALPHABET

with open(sys.argv[1], 'r') as lines:
    for line in lines:
        output = ''
        i = 1
        for char in line:

            if char.lower() in ALPHABET:
                if i % 2 == 0:
                    output_char = char.lower()
                else:
                    output_char = char.upper()
                i += 1
            else:
                output_char = char

            output += output_char

        print(output)
