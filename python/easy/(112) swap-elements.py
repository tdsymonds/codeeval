import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(' : ')

                number_list = line[0].split(' ')
                swaps = [x.split('-') for x in line[1].split(', ')]

                for swap in swaps:
                    swap1 = int(swap[0])
                    swap2 = int(swap[1])

                    number_list[swap1], number_list[swap2] = number_list[swap2], number_list[swap1]

                print ' '.join(number_list)


if __name__ == '__main__':
    main(sys.argv[1])
