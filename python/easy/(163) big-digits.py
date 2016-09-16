import sys

NUMBER_DICT = {
    '0': """-**--
          *--*-
          *--*-
          *--*-
          -**--
          -----""",
    '1': """--*--
          -**--
          --*--
          --*--
          -***-
          -----""",
    '2': """***--
          ---*-
          -**--
          *----
          ****-
          -----""",

    '3': """***--
          ---*-
          -**--
          ---*-
          ***--
          -----""",

    '4': """-*---
          *--*-
          ****-
          ---*-
          ---*-
          -----""",

    '5': """****-
          *----
          ***--
          ---*-
          ***--
          -----""",

    '6': """-**--
          *----
          ***--
          *--*-
          -**--
          -----""",

    '7': """****-
          ---*-
          --*--
          -*---
          -*---
          -----""",

    '8': """-**--
          *--*-
          -**--
          *--*-
          -**--
          -----""",

    '9': """-**--
          *--*-
          -***-
          ---*-
          -**--
          -----""",
}

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()

                big_digits_string = ''

                for i in xrange(6):
                    for char in line:
                        if unicode(char).isnumeric():
                            big_digit = NUMBER_DICT[char]
                            big_digit = big_digit.split('\n')
                            big_digits_string += big_digit[i].strip()
                    big_digits_string += '\n'

                print big_digits_string

if __name__ == '__main__':
    main(sys.argv[1])
