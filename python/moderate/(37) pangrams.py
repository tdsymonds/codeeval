import sys
import string

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                print missing_letters(line)

def missing_letters(sentance):
    alphabet = list(string.ascii_lowercase)
    sentance = list(sentance.lower().replace(' ', ''))

    result = ''.join(sorted(set(alphabet) - set(sentance)))
    if not result:
        return 'NULL'
    return result


if __name__ == '__main__':
    main(sys.argv[1])