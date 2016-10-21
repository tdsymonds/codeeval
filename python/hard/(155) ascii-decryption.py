from string import ascii_letters as alphabet
import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(' | ')

                word_length = int(line[0])
                last_letter = line[1]
                encrypted_message = map(int, line[2].split(' '))

                keys = []

                for i in xrange(len(encrypted_message)-word_length):
                    sublist = encrypted_message[i:word_length+i]
                    rest_of_list = encrypted_message[word_length+i:]

                    if getsubidx(rest_of_list, sublist):
                        diff = sublist[-1] - ord(last_letter)
                        result = ''
                        for x in sublist:
                            new_i = x - diff
                            if new_i in range(256):
                                if chr(new_i) in alphabet:
                                    result += chr(new_i)
                                else:
                                    result = ''
                                    break
                            else:
                                result = ''
                                break

                        if result:
                            keys.append(diff)

                # I'm assuming that only one result will be returned
                # which worked in this instance. Wanted to do this
                # before adding additional complexity unnecessarily.
                deciphered_message = []
                for char in encrypted_message:
                    deciphered_message.append(chr(char-keys[0]))

                print ''.join(deciphered_message)

def getsubidx(x, y):
    l1, l2 = len(x), len(y)
    for i in range(l1):
        if x[i:i+l2] == y:
            return i

if __name__ == '__main__':
    main(sys.argv[1])