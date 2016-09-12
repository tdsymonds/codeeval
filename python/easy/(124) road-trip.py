import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(';')[:-1]

                distances = []
                for city in line:
                    city = city.strip()
                    city = city.split(',')
                    distances.append(int(city[1]))

                distances_between = []

                point = 0
                distances = sorted(distances)
                
                for distance in distances:
                    distances_between.append(str(distance - point))
                    point = distance

                print ','.join(distances_between)


if __name__ == '__main__':
    main(sys.argv[1])
