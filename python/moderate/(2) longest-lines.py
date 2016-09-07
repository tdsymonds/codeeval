from operator import itemgetter
import sys

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

    # set initial variables
    word_list = []
    output_lines = int(lines[0])

    # loop through rest of the words
    # after output lines
    for line in lines[1:]:
        # get word length and word
        word_list.append([line, len(line)])

    # sort descending by word length
    sorted_word_list = sorted(word_list, key=itemgetter(1), reverse=True)

    # print results
    for line in sorted_word_list[:output_lines]:
        print line[0]

        