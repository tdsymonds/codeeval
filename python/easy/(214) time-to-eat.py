from datetime import datetime
import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            line = line.split(' ')
            sorted_times = sorted([datetime.strptime(x, '%H:%M:%S') for x in line], reverse=True)
            for time in sorted_times:
                print time.strftime('%H:%M:%S'),
            print