import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(' | ')
                
                players = line[0].split(' ')
                number = int(line[1])
                number_of_players = len(players)

                i = 0
                while number_of_players > 1:
                    if (i+1) % number == 0:
                        del players[i % number_of_players]
                        number_of_players -= 1
                        i = 0
                    i += 1

                print players[0]

if __name__ == '__main__':
    main(sys.argv[1])
