import math
import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(' ')

                m = Matrix(line)
                m.rotate()
                print ' '.join(m.serialized_matrix)

class Matrix:
    def __init__(self, serialized_matrix):
        self.serialized_matrix = serialized_matrix

    def rotate(self):
        n = int(math.sqrt(len(self.serialized_matrix)))
        rotated_matrix = []

        for i in xrange(n,0,-1):
            for j in xrange(n,0,-1):
                rotated_matrix.append(self.serialized_matrix[j*n-i])

        self.serialized_matrix = rotated_matrix

if __name__ == '__main__':
    main(sys.argv[1])
