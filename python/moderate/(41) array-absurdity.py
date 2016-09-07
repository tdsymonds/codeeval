import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            line = line.split(';')
            n = int(line[0])
            n_array = map(int, line[1].split(','))
            rng = range(n-1)
            for elm in n_array:
                if elm not in rng: 
                    print elm
                    break
                rng.remove(elm)