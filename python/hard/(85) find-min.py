import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip().split(',')
                
                n = int(line[0])
                k = int(line[1])
                a = int(line[2])
                b = int(line[3])
                c = int(line[4])
                r = int(line[5])
    
                m = getKnownValues(a, b, c, r, k)
                m = getUnknownValues(k, n, m)
                
                print m[-1]

def getKnownValues(a, b, c, r, k):
    m = [a]
    for i in xrange(1,k):
        m.append((b * m[i-1] + c) % r)
    return m

def getUnknownValues(k, n, m):
    for j in range(k, n):
        m.append(min(set(range(j))-set(m[j-k:])))
    return m

if __name__ == '__main__':
    main(sys.argv[1])