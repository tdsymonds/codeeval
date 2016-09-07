import sys

def main():
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                print ' '.join(map(str, pascals_triangle(int(line))))

def pascals_triangle(number):
    triangle = []
    for i in xrange(number):
        line = [1]
        for j in xrange(i):
            line.append(line[j]*(i-j)/(j+1))
        triangle += line
    return triangle

if __name__ == '__main__':
    main()