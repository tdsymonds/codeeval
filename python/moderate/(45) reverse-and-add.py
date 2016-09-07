import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                number_str = line.strip()
                i = 0
                found = False

                while(i < 100 and not found):
                    new_number = int(number_str) + int(number_str[::-1])
                    number_str = str(new_number)
                    if is_palindrome(new_number):
                        found = True
                    i += 1

                if found:
                    print i, new_number

def is_palindrome(number):
    """
    Returns true if a number is a palindrome.
    """
    number_string = str(number)
    number_length = len(number_string)
    
    # set the default cutpoints
    cutpoint = number_length / 2
    first_partition = number_string[:cutpoint]
    second_partition = number_string[cutpoint:]
    
    # if odd need to cut the middle number
    # out of the partitions
    if number_length % 2 != 0:
        second_partition = number_string[cutpoint + 1:]
    
    # do the partitions match?
    if first_partition == second_partition[::-1]:
        # have a palindrome!
        return True

    # no palindrome
    return False


if __name__ == '__main__':
    main(sys.argv[1])