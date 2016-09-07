import sys

with open(sys.argv[1], 'r') as file:
    
    lines = file.readlines()

    for line in lines:
        
        line_to_print = []
        line_list = line.split()
        
        f = int(line_list[0])
        b = int(line_list[1])
        n = int(line_list[2])
    
        for i in xrange(1, n+1):
            if i % f == 0 and i % b == 0:
                line_to_print.append('FB')
            elif i % f == 0:
                line_to_print.append('F')
            elif i % b == 0:
                line_to_print.append('B')
            else:
                line_to_print.append(str(i))
        
        print ' '.join(line_to_print)