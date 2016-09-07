import math
import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(';')
                
                n = int(line[0])
                grid = map(int, line[1].split(','))
    
                s = SodukuGrid(n, grid)
                print s.isValid()


class SodukuGrid:
    def __init__(self, size, grid):
        self.size = size
        self.grid = grid

    def isValid(self):
        rows_are_valid = self._rowsAreValid()
        cols_are_valid = self._columnsAreValid()
        regions_are_valid = self._regionsAreValid()
        return rows_are_valid and cols_are_valid and regions_are_valid

    def _rowsAreValid(self):
        row_nums = []
        valid = True
        num_range = range(1,self.size+1)

        for i, num in enumerate(self.grid):
            row_nums.append(num)
            if (i+1) % self.size == 0:
                if not sorted(row_nums) == num_range:
                    valid = False
                    break
                row_nums = []
        return valid

    def _columnsAreValid(self):
        valid = True
        num_range = range(1,self.size+1)

        for i in xrange(self.size):
            col_nums = []
            for j in xrange(self.size):
                col_nums.append(self.grid[i+(j*self.size)])
            if not sorted(col_nums) == num_range:
                valid = False
                break
        return valid

    def _regionsAreValid(self):        
        valid = True
        num_range = range(1,self.size+1)

        region_size = int(math.sqrt(self.size))
        region_spacer = region_size ** 3 - self.size

        # loop through each region
        for i in xrange(self.size):
            region_nums = []
            # loop through each line in the region
            for j in xrange(region_size):
                starting_index = (i*region_size)+(j*self.size)+(i//region_size*region_spacer)
                ending_index = starting_index + region_size
                region_nums += self.grid[starting_index:ending_index]
            if not sorted(region_nums) == num_range:
                valid = False
                break
        return valid


if __name__ == '__main__':
    main(sys.argv[1])
