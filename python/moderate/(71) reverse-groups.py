import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(';')
                
                lst = line[0].split(',')
                j = k = int(line[1])

                i = 0
                new_lst = []

                while i < len(lst):
                    elms = lst[i:j]
                    if len(elms) is not k:
                        new_lst += elms
                    else:
                        new_lst += elms[::-1]

                    i += k
                    j += k

                print ','.join(new_lst)

if __name__ == '__main__':
    main(sys.argv[1])