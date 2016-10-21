import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                print get_category(int(line))


def get_category(age):
    if age < 0 or age > 100:
        return 'This program is for humans'        
    if age < 3:
        return "Still in Mama's arms"
    if age < 5:
        return 'Preschool Maniac'
    if age < 12:
        return 'Elementary school'
    if age < 15:
        return 'Middle school'
    if age < 19:
        return 'High school'
    if age < 23:
        return 'College'
    if age < 66:
        return 'Working for the man'
    if age < 100:
        return 'The Golden Years'

if __name__ == '__main__':
    main(sys.argv[1])
