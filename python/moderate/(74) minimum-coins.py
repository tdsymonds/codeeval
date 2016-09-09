import sys

def main(filepath):
    
    COINS = [1,3,5]

    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                total = int(line)

                number_of_coins = 0
                total_so_far = 0
                i = 1
        
                while total_so_far < total:
                    coin = COINS[-i]
                    if total_so_far + coin > total:
                        i += 1
                    else:
                        total_so_far += coin
                        number_of_coins += 1
        
                print number_of_coins


if __name__ == '__main__':
    main(sys.argv[1])
