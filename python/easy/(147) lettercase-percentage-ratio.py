from __future__ import division
import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                
                total = len(line)
                lower = 0
                upper = 0

                for char in line:
                    if char.islower():
                        lower += 1
                    else:
                        upper += 1

                print 'lowercase: %.2f uppercase: %.2f' % (lower/total*100, upper/total*100)

if __name__ == '__main__':
    main(sys.argv[1])
