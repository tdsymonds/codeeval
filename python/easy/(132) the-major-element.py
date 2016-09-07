import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                
                sequence = line.split(',')
                l = len(sequence)
                target_count = l//2
                
                count_dict = {}
                major_elm = None

                for elm in sequence:
                    if elm in count_dict:
                        count_dict[elm] += 1
                        if count_dict[elm] > target_count:
                            # found the major elm so break
                            major_elm = elm
                            break
                    else:
                        count_dict[elm] = 1

                print major_elm

if __name__ == '__main__':
    main(sys.argv[1])