import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(' ')

                word_list = []

                for word in line:
                    first_num = word[0]
                    last_num = word[-1]
                    word_list.append(last_num + word[1:-1] + first_num)

                print ' '.join(word_list)

if __name__ == '__main__':
    main(sys.argv[1])
