import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(' ')
                
                n = int(line[0])
                m = int(line[1])

                doors = {x: False for x in xrange(1,n+1)}
                
                for i in xrange(m-1):
                    doors = start_beat(doors)

                doors[n] = reverse_boolean(doors[n])

                print len([k for k, v in doors.iteritems() if not v]) 


def start_beat(doors):
    for k, v in doors.iteritems():
        if k % 2 == 0:
            doors[k] = True
    for k, v in doors.iteritems():
        if k % 3 == 0:
            doors[k] = reverse_boolean(v)
    return doors


def reverse_boolean(b):
    if b:
        return False
    return True


if __name__ == '__main__':
    main(sys.argv[1])
