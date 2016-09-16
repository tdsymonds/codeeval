from string import ascii_uppercase as alphabet
import sys


def main():
    message = '012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119'
    key = 'BHISOECRTMGWYVALUZDNFJKPQX'

    decoded_message = []

    for word in message.split(' '):
        pairs = [word[i:i+2] for i in xrange(0,len(word),2)]
        for pair in pairs:
            decoded_message.append(alphabet[key.index(alphabet[int(pair)])])
        decoded_message.append(' ')

    print ''.join(decoded_message)


if __name__ == '__main__':
    main()
