from datetime import datetime
import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(' ')

                time1 = datetime.strptime(line[0], '%H:%M:%S')
                time2 = datetime.strptime(line[1], '%H:%M:%S')
                
                result = time1 - time2
                if result.total_seconds() < 0:
                    result = time2 - time1
                
                result = str(result)
                if len(result[:result.find(':')]) == 1:
                    result = '0' + result
                print result

if __name__ == '__main__':
    main(sys.argv[1])
