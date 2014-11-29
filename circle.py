import argparse 
import random
import sys
import svgwrite
import cairosvg

class Circle(object):
    def __init__(self):
        self.colors = ['#4d4d4d','#0000ff','#0066ff']
        self.c = random.randint(0, 2)
        self.cx =random.randint(0, 400)
        self.cy = random.randint(0, 300)
        self.r = random.randint(1, 200)

    def define (self, 
            dwg, 
            stroke=None, 
            fill=None,
            cx=None, 
            cy=None,
            r=None):
        stroke = stroke or self.colors[self.c]
        fill = fill or stroke
        cx = cx or self.cx
        cy = cy or self.cy
        r = r or self.r

        return dwg.add(dwg.circle(
            (cx, cy), 
            r,
            stroke=stroke,
            fill=fill))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-svg", type=str, help="svg file name", default="circle")
    parser.add_argument("-png", type=str, help="png file name", default="circle")
    parser.add_argument("-w", type=int, help="Image width", default=400)
    parser.add_argument("-he", type=int, help="Image height", default=300)
    args = parser.parse_args()
    svg = '%s.svg' % (args.svg)
    png = '%s.png' % (args.png)
    w = '%ipx' % (args.w)
    h = '%ipx' % (args.he)
    dwg = svgwrite.Drawing(filename = svg, size = (w, h))
    circle = Circle()
    circle.define(dwg)
    dwg.save()
    fout = open(png,'w')
    with open(svg, 'r') as f:
        svg_file = f.read()
    f.closed
    cairosvg.svg2png(bytestring=svg_file,write_to=fout)
    fout.close()