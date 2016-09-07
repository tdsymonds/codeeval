import sys


def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                print number_in_words(int(line)) + 'Dollars'    


def number_in_words(number):

    # set the word lists
    numbers = ['Zero', 'One', 'Two', 'Three',
        'Four', 'Five', 'Six', 'Seven', 'Eight',
        'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen',
        'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',
        'Eighteen', 'Nineteen',]

    tens_words = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty',
        'Sixty', 'Seventy', 'Eighty', 'Ninety',]

    power_words = ['Hundred', 'Thousand', 'Million',]

    # initialise empty result
    result = ''

    # how many millions?
    millions = number // 10**6
    number -= millions * 10**6
    if millions > 0:
        result += number_in_words(millions) + power_words[2]
        
    # how many thousands?
    thousands = number // 10**3
    number -= thousands * 10**3
    if thousands > 0:
        result += number_in_words(thousands) + power_words[1]
    
    # how many hundreds?
    hundreds = number // 10**2
    number -= hundreds * 10**2
    if hundreds > 0:
        result += numbers[hundreds] + power_words[0]

    # how many tens?
    tens = number // 10
    if tens > 1:
        number -= tens * 10
        result += tens_words[tens-1]

    # how many singles?
    singles = number
    if singles > 0:
        result += numbers[singles]
    elif result == '' and singles == 0:
        result = numbers[singles]   

    return result


if __name__ == '__main__':
    main(sys.argv[1])