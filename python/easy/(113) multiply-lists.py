import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(' | ')

                list1 = line[0].split(' ')
                list2 = line[1].split(' ')

                for i in xrange(len(list1)):
                    print int(list1[i]) * int(list2[i]),
                print


if __name__ == '__main__':
    main(sys.argv[1])
