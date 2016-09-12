import sys

def main(filepath):
    # with open(filepath, 'r') as f:
    #     for line in f.readlines():
    #         if line:
    #             line = line.strip()


    lines = """5
        12"""

    lines = lines.split('\n')

    the_sum = 0

    for line in lines:
        if line:
            line = line.strip()
            the_sum += int(line)

    print the_sum




if __name__ == '__main__':
    # main(sys.argv[1])
    main(None)
