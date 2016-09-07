import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = map(int, line.strip().split(' '))

                differences = []

                n = len(line)
                for i in xrange(n-1):
                    differences.append(abs(line[i]-line[i+1]))

                if len(set(range(1,n-1)) - set(differences)) == 0:
                    print 'Jolly'
                else:
                    print 'Not jolly'


if __name__ == '__main__':
    main(sys.argv[1])