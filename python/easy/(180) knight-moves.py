import string
import sys


def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                print ' '.join(get_moves(line))


def get_moves(position):
    col = position[0]
    row = int(position[1])

    columns = string.ascii_lowercase[:8]
    rows = range(1,9)

    moves = []

    for i in xrange(-2,3):
        if i != 0:
            col_index = columns.index(col) + i
            if 0 <= col_index < 8:
                if i in [-2,2]:
                    for j in [-1,1]:
                        row_index = row + j -1
                        if 0 <= row_index < 8:
                            moves.append(columns[col_index] + str(rows[row_index]))

                elif i in [-1,1]:
                    for j in [-2,2]:
                        row_index = row + j -1
                        if 0 <= row_index < 8:
                            moves.append(columns[col_index] + str(rows[row_index]))
        
    return moves


if __name__ == '__main__':
    main(sys.argv[1])
