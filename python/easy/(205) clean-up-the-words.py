import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()

                cleaned_line = ''.join([c.lower() if c.isalpha() else ' ' for c in line])
                print ' '.join(filter(None, cleaned_line.split(' ')))

if __name__ == '__main__':
    main(sys.argv[1])
