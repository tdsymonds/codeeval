import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()

                for char in line:
                    if line.count(char) == 1:
                        print char
                        break
        
if __name__ == '__main__':
    main(sys.argv[1])
