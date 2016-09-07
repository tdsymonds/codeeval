import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(',')
                
                a = map(int, line[:4])
                b = map(int, line[4:])
                
                r1 = Rectangle(a[:2], a[2:])
                r2 = Rectangle(b[:2], b[2:])

                print r1.intersects_with(r2)

class Rectangle:
    def __init__(self, upper_left, lower_right):
        self.upper_left = upper_left
        self.lower_right = lower_right

    def __str__(self):
        return '%s, %s' % (self.upper_left, self.lower_right)

    def get_upper_y(self):
        return self.upper_left[1]

    def get_lower_y(self):
        return self.lower_right[1]

    def get_left_x(self):
        return self.upper_left[0]

    def get_right_x(self):
        return self.lower_right[0]

    def intersects_with(self, rectangle):
        intersect_vertically = False
        if ((self.get_lower_y() <= rectangle.get_upper_y() <= self.get_upper_y()) or 
            (self.get_lower_y() <= rectangle.get_lower_y() <= self.get_upper_y())):
            intersect_vertically = True

        intersect_horizontally = False
        if ((self.get_left_x() <= rectangle.get_left_x() <= self.get_right_x()) or
            (self.get_left_x() <= rectangle.get_right_x() <= self.get_right_x())):
            intersect_horizontally = True

        return intersect_vertically and intersect_horizontally


if __name__ == '__main__':
    main(sys.argv[1])