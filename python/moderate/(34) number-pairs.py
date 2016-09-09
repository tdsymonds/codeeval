import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(';')

                x = int(line[1])
                sorted_numbers = map(int, line[0].split(','))

                pairs = []

                for number in sorted_numbers:
                    paired_number = x - number
                    if number == paired_number and sorted_numbers.index(number) == sorted_numbers.index(paired_number):
                        continue
                    if paired_number in sorted_numbers:
                        pairs.append(sorted([number, paired_number]))

                if pairs:
                    result_list = []
                    for pair in pairs:
                        pair_string = ','.join(map(str, pair))
                        if pair_string not in result_list:
                            result_list.append(pair_string)
                    print ';'.join(result_list)
                else:
                    print 'NULL'


if __name__ == '__main__':
    main(sys.argv[1])
