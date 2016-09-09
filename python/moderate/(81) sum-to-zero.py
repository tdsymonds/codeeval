from itertools import combinations
import sys


def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                integer_list = map(int, line.split(','))
                
                count = 0
                for c in combinations(integer_list, 4):
                    if sum(c) == 0:
                        count += 1
    
                print count

             
if __name__ == '__main__':
    main(sys.argv[1])
