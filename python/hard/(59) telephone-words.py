from itertools import product
import sys

MAPPING_DICT = {
    '0' : '0',
    '1' : '1',
    '2' : 'abc',
    '3' : 'def',
    '4' : 'ghi',
    '5' : 'jkl',
    '6' : 'mno',
    '7' : 'pqrs',
    '8' : 'tuv',
    '9' : 'wxyz',
}

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
   
                lists = [list(MAPPING_DICT[x]) for x in line]
                word_lists = list(product(*lists))

                print ','.join([''.join(x) for x in word_lists])

if __name__ == '__main__':
    main(sys.argv[1])
