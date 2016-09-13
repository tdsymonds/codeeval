import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(' | ')

                developer_text = line[0]
                design_text = line[1]

                bugs = 0
                for i, char in enumerate(developer_text):
                    if char is not design_text[i]:
                        bugs += 1

                print prioritize_bugs(bugs) 

def prioritize_bugs(n):
    if n == 0:
        return 'Done'
    if n <= 2:
        return 'Low'
    if n <= 4:
        return 'Medium'
    if n <= 6:
        return 'High'
    return 'Critical'

if __name__ == '__main__':
    main(sys.argv[1])
