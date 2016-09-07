import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                
                count_dict = {}

                for char in line:
                    if char.isalpha():
                        char = char.lower()
                        if char in count_dict:
                            count_dict[char] += 1
                        else:
                            count_dict[char] = 1

                sorted_counts = sorted(count_dict.items(), key=lambda kv: kv[1], reverse=True)

                max_beauty_of_string = 0
                max_beauty_rating = 26

                for elm in sorted_counts:
                    max_beauty_of_string += elm[1] * max_beauty_rating
                    max_beauty_rating -= 1

                print max_beauty_of_string


if __name__ == '__main__':
    main(sys.argv[1])