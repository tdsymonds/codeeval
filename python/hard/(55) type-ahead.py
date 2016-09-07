from __future__ import division

import sys

def main(filepath):

    WORD_LIST = ['Mary', 'had', 'a', 'little', 'lamb', 'its', 'fleece', 'was',
                 'white', 'as', 'snow', 'And', 'everywhere', 'that', 'Mary',
                 'went', 'the', 'lamb', 'was', 'sure', 'to', 'go', 'It',
                 'followed', 'her', 'to', 'school', 'one', 'day', 'which', 'was',
                 'against', 'the', 'rule', 'It', 'made', 'the', 'children',
                 'laugh', 'and', 'play', 'to', 'see', 'a', 'lamb', 'at', 'school',
                 'And', 'so', 'the', 'teacher', 'turned', 'it', 'out', 'but',
                 'still', 'it', 'lingered', 'near', 'And', 'waited', 'patiently',
                 'about', 'till', 'Mary', 'did', 'appear', 'Why', 'does', 'the',
                 'lamb', 'love', 'Mary', 'so', 'the', 'eager', 'children', 'cry',
                 'Why', 'Mary', 'loves', 'the', 'lamb', 'you', 'know', 'the',
                 'teacher', 'did', 'reply']


    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(',')
                            
                ngram_length = int(line[0])
                user_text = line[1]

                ngrams = getNgrams(WORD_LIST, ngram_length)
                
                count_dict = {}
            
                for tple in ngrams:
                    key = ' '.join(tple[:ngram_length-1])
                    if key == user_text:
                        word = tple[-1]
                        if word in count_dict:
                            count_dict[word] += 1
                        else:
                            count_dict[word] = 1
            
                sorted_results = sorted(count_dict.items(), key=lambda e: (-e[1], e[0]))
                total_number_of_words = sum(count_dict.values())
            
                result_string = ''
                for result in sorted_results:
                    result_string += '%s,%.3f;' % (result[0], (result[1]/total_number_of_words))
            
                print result_string[:-1]

def getNgrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

if __name__ == '__main__':
    main(sys.argv[1])
