import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip().split(';')
                n = int(line[0].split(',')[1])
                row = line[1]
        
                m = MineSweeper(n, row)
                print m.solve()

class MineSweeper:
    def __init__(self, n, row):
        self.n = n
        self.row = row
        self.solved = []

    def solve(self):
        for index, elm in enumerate(self.row):
            if elm == '*':
                self.solved.append(elm)
            else:
                number = 0
                               
                number += self._isMineAtIndex(index, index-1, 0)
                number += self._isMineAtIndex(index, index-self.n-1, 0)
                number += self._isMineAtIndex(index, index+self.n-1, 0)

                number += self._isMineAtIndex(index, index-self.n, -1)
                number += self._isMineAtIndex(index, index+self.n, -1)

                number += self._isMineAtIndex(index, index+1, self.n-1)
                number += self._isMineAtIndex(index, index-self.n+1, self.n-1)
                number += self._isMineAtIndex(index, index+self.n+1, self.n-1)

                self.solved.append(number)
                
        return ''.join(map(str, self.solved))

    def _isMineAtIndex(self, index, target_index, remainder):
        if (target_index >= 0 and 
                target_index < (len(self.row)) and 
                index % self.n != remainder and 
                self.row[target_index] == '*'):
            return 1
        return 0

if __name__ == '__main__':
    main(sys.argv[1])

