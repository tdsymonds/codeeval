import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(' ')
                
                longest_word = ''
                for word in line:
                    if len(word) > len(longest_word):
                        longest_word = word

                print longest_word


if __name__ == '__main__':
    main(sys.argv[1])
