import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                print is_luhn_valid(line)

def digits_of(number):
    return [int(i) for i in str(number) if i is not ' ']

def luhn_checksum(card_number):
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for digit in even_digits:
        total += sum(digits_of(2 * digit))
    return total % 10

def is_luhn_valid(card_number):
    if luhn_checksum(card_number) == 0:
        return 1
    return 0

if __name__ == '__main__':
    main(sys.argv[1])
