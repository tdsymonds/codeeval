import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                print is_card_real(line.replace(' ', ''))

def is_card_real(num_str):   
    doubled_num_sum = 0
    other_sum = 0
    
    for i, char in enumerate(num_str):
        if (i+1) % 2 == 0:
            other_sum += int(char)
        else:
            doubled_num_sum += int(char) * 2

    total_sum = doubled_num_sum + other_sum

    if total_sum % 10 == 0:
        return 'Real'
    return 'Fake'

if __name__ == '__main__':
    main(sys.argv[1])
