import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(';')
                
                n = int(line[0])
                m = int(line[1])
                serialized_matrix = line[2].split(' ')

                matrix = Matrix(serialized_matrix, n, m)
                print ' '.join(matrix.get_spiral())
            
class Matrix:
    def __init__(self, serialized_matrix, n, m):
        self.serialized_matrix = serialized_matrix
        self.n = n
        self.m = m

    def get_matrix(self):
        """
        matrix[y][x]
        """
        matrix = [[0 for x in xrange(self.m)] for y in xrange(self.n)]
        for i, char in enumerate(self.serialized_matrix):
            quotient, remainder = divmod(i, self.m)
            matrix[quotient][remainder] = char
        return matrix

    def get_spiral(self):
        
        def is_empty(m):
            empty = True
            for x in m:
                for y in x:
                    if y:
                        empty = False
                        break

            return empty

        t = 0
        l = 0
        b = self.n-1
        r = self.m-1

        matrix = self.get_matrix()
        spiralled_values = []

        while not is_empty(matrix):
            # move along the top
            for i in xrange(self.m):
                if matrix[t][i]:
                    spiralled_values.append(matrix[t][i])
                    matrix[t][i] = None
            
            # move along the right
            for i in xrange(self.n):
                if matrix[i][r]:
                    spiralled_values.append(matrix[i][r])
                    matrix[i][r] = None
            
            # move along the bottom
            for i in xrange(self.m-1,0,-1):
                if matrix[b][i]:
                    spiralled_values.append(matrix[b][i])
                    matrix[b][i] = None

            # move along the left
            for i in xrange(self.n-1,0,-1):
                if matrix[i][l]:
                    spiralled_values.append(matrix[i][l])
                    matrix[i][l] = None
                
            # bring in the four sides            
            t += 1
            r -= 1
            b -= 1
            l += 1 

        return spiralled_values

if __name__ == '__main__':
    main(sys.argv[1])
