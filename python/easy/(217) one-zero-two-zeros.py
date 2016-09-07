import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip().split(' ')
                
                number_of_zeros = int(line[0])
                max_range = int(line[1])

                counter = 0

                for i in xrange(1,max_range+1):
                    binary_string = str(bin(int(i)))[2:]
                    zero_counter = 0

                    for char in binary_string:
                        if char == '0':
                            zero_counter += 1
                            if zero_counter > number_of_zeros:
                                # too many zeros so no need to look further
                                break

                    if zero_counter == number_of_zeros:
                        counter += 1

                print counter


if __name__ == '__main__':
    main(sys.argv[1])