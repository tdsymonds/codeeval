import operator
import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(' ')

                n = line[0]
                pattern = line[1]

                add = evaluate(n, pattern, '+')
                if add:
                    print add
                else:
                    print evaluate(n, pattern, '-')

def evaluate(n, pattern, op_char):
    ops = {'+': operator.add, 
        '-': operator.sub}
    index = pattern.find(op_char)
    if index > -1:
        op_func = ops[op_char]
        return op_func(int(n[:index]), int(n[index:]))
    return None

if __name__ == '__main__':
    main(sys.argv[1])
