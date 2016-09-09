import math
import sys


def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split('; ')
    
                center = line[0].split(': ')[1]
                center = map(float, center[1:-1].split(', '))
    
                radius = float(line[1].split(': ')[1])
    
                point = line[2].split(': ')[1]
                point = map(float, point[1:-1].split(', '))
    
                x = point[0] - center[0]
                y = point[1] - center[1]
    
                if math.sqrt(x**2+y**2) <= radius:
                    print 'true'
                else:
                    print 'false'


if __name__ == '__main__':
    main(sys.argv[1])
