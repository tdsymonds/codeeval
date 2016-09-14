from itertools import permutations
import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                perms = permutations(line)
                results = [''.join(x) for x in perms]
                print ','.join(sorted(results))

if __name__ == '__main__':
    main(sys.argv[1])
