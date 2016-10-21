import sys

RIGHT_ARROW = '>>-->'
LEFT_ARROW = '<--<<'            

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                count = 0

                for i in xrange(len(line)):
                    arrow = line[i:i+5]
                    if arrow == LEFT_ARROW or arrow == RIGHT_ARROW:
                        count += 1

                print count            
        
if __name__ == '__main__':
    main(sys.argv[1])
