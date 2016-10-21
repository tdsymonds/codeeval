from __future__ import division
import colorsys
import sys


def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                print convert_to_rgb(line)

def convert_to_rgb(colour_code):
    if colour_code[0] == '#':
        return format_rgb_to_print(hex_to_rgb(colour_code))
    if colour_code[0] == '(':
        return format_rgb_to_print(cmyk_to_rgb(colour_code))
    if colour_code[:3] == 'HSL':
        return format_rgb_to_print(hsl_to_rgb(colour_code))
    if colour_code[:3] == 'HSV':
        return format_rgb_to_print(hsv_to_rgb(colour_code))

def hex_to_rgb(colour_code):
    hex_list = chunks(colour_code[1:], 2)
    return [str(int(x, 16)) for x in hex_list]

def cmyk_to_rgb(colour_code):
    colour_code = colour_code[1:-1].split(',')

    c = float(colour_code[0])
    m = float(colour_code[1]) 
    y = float(colour_code[2])
    k = float(colour_code[3])
    
    return [
        stringify(255*(1-c)*(1-k)),
        stringify(255*(1-m)*(1-k)),
        stringify(255*(1-y)*(1-k)),
    ]

def hsl_to_rgb(colour_code):
    colour_code = colour_code[4:-1].split(',')
    
    h = float(colour_code[0])/360
    s = float(colour_code[1])/100
    l = float(colour_code[2])/100

    r,g,b = colorsys.hls_to_rgb(h,l,s)

    return [
        stringify(255*r),
        stringify(255*g),
        stringify(255*b),
    ]

def hsv_to_rgb(colour_code):
    colour_code = colour_code[4:-1].split(',')

    h = float(colour_code[0])/360
    s = float(colour_code[1])/100
    v = float(colour_code[2])/100

    r,g,b = colorsys.hsv_to_rgb(h,s,v)

    return [
        stringify(255*r),
        stringify(255*g),
        stringify(255*b),
    ]

def stringify(num):
    return str(int(round(num,0)))

def format_rgb_to_print(rgb_list):
    return 'RGB(%s)' % ','.join(rgb_list)

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':
    main(sys.argv[1])
