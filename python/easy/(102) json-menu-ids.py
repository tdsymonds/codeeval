import json
import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                data = json.loads(line)
                the_sum = 0
                for item in data['menu']['items']:
                    if item:
                        if 'label' in item:
                            the_sum += int(item['id'])

                print the_sum


if __name__ == '__main__':
    main(sys.argv[1])
