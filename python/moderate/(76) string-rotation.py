import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line:
            line = line.strip()
            line = line.split(',')
    
            word1 = line[0]
            word2 = line[1]

            found = False
            for i in range(len(word2)):
                if (word2[i:] + word2[:i]) == word1:
                    found = True
                    break

            print found

