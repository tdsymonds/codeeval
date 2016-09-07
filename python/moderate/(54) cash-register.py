from decimal import Decimal
import sys

def main():
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip().split(';')
                pp = Decimal(line[0])
                ch = Decimal(line[1])
                print change_in_money(pp, ch)

def change_in_money(purchase_price, cash):
    money_dict = {
        1: 'PENNY',
        5: 'NICKEL',
        10: 'DIME',
        25: 'QUARTER',
        50: 'HALF DOLLAR',
        100: 'ONE',
        200: 'TWO',
        500: 'FIVE',
        1000: 'TEN',
        2000: 'TWENTY',
        5000: 'FIFTY',
        10000: 'ONE HUNDRED'
    }
    money_keys = sorted(money_dict.keys(), reverse=True)

    if cash < purchase_price:
        return 'ERROR'
    
    change_due = cash - purchase_price
    change_due = int(change_due*100)
    
    if change_due == 0:
        return 'ZERO'

    change_words = []
    
    while change_due > 0:
        for key in money_keys:
            if key <= change_due:
                change_words.append(money_dict[key])
                change_due -= key
                break

    return ','.join(change_words)

if __name__ == '__main__':
    main()