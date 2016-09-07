import sys

def main():
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            print fibonacci(int(line))

def fibonacci(n, calculated={0: 0, 1: 1}):
    if n not in calculated:
        calculated[n] = fibonacci(n-1, calculated) + fibonacci(n-2, calculated)
    return calculated[n]

if __name__ == '__main__':
    main()