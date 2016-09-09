import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(' ')
            
                line = map(int, line)
                sorted_line = sorted(line)
            
                answer = 0
            
                for num in sorted_line:
                    if sorted_line.count(num) == 1:
                        answer = line.index(num)+1
                        break
            
                print answer          
            
if __name__ == '__main__':
    main(sys.argv[1])
