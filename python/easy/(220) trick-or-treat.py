import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(', ')

                vampires = int(line[0].split(': ')[1])
                zombies = int(line[1].split(': ')[1])
                witches = int(line[2].split(': ')[1])
                houses = int(line[3].split(': ')[1])

                print int((vampires * 3 + zombies * 4 + witches * 5) * houses / sum([vampires, zombies, witches]))

if __name__ == '__main__':
    main(sys.argv[1])
