import string
import sys


def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(';')

                hints = map(int, line[1].split(' '))
                sentance = line[0].split(' ')

                original_sentance = [None] * len(sentance)
                
                for i, hint in enumerate(hints):
                    original_sentance[hint-1] = sentance[i]

                original_sentance[original_sentance.index(None)] = sentance[-1]

                print ' '.join(original_sentance)


if __name__ == '__main__':
    main(sys.argv[1])
