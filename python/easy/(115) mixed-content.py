import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(',')
                
                word_list = []
                digit_list = []

                for elm in line:
                    if elm.isdigit():
                        digit_list.append(elm)
                    else:
                        word_list.append(elm)

                if word_list and digit_list:
                    print ('%s|%s') % (','.join(word_list), ','.join(digit_list))
                elif word_list and not digit_list:
                    print ','.join(word_list)
                elif not word_list and digit_list:
                    print ','.join(digit_list)

              
if __name__ == '__main__':
    main(sys.argv[1])
