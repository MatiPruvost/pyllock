import argparse
import random
import sys
import svgwrite
import cairosvg

class Line(object):
    def __init__(self):
        self.colors = ['#4d4d4d','#0000ff','#0066ff']
        self.c = random.randint(0, 2)
        self.x1 =random.randint(0, 400)
        self.x2 =random.randint(0, 400)
        self.y1 = random.randint(0, 300)
        self.y2 = random.randint(0, 300)
        self.stroke_linecap = "round"
        self.stroke_width = random.randint(1, 20)

    def define (self, 
            dwg, 
            color=None, 
            x1=None, 
            x2=None, 
            y1=None,
            y2=None,
            stroke_linecap=None,
            stroke_width=None):
        color = color or self.colors[self.c]
        x1 = x1 or self.x1
        x2 = x2 or self.x2
        y1 = y1 or self.y1
        y2 = y2 or self.y2
        stroke_width = stroke_width or self.stroke_width
        stroke_linecap = stroke_linecap or self.stroke_linecap

        return dwg.add(dwg.line(
            (x1, y1), 
            (x2, y2), 
            stroke_width=stroke_width,
            stroke_linecap=stroke_linecap,
            stroke=color))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-svg", type=str, help="svg file name", default="line")
    parser.add_argument("-png", type=str, help="png file name", default="line")
    parser.add_argument("-w", type=int, help="Image width", default=400)
    parser.add_argument("-he", type=int, help="Image height", default=300)
    args = parser.parse_args()
    svg = '%s.svg' % (args.svg)
    png = '%s.png' % (args.png)
    w = '%ipx' % (args.w)
    h = '%ipx' % (args.he)
    dwg = svgwrite.Drawing(filename = svg, size = (w, h))
    line = Line()
    line.define(dwg)
    dwg.save()
    fout = open(png,'w')
    with open(svg, 'r') as f:
        svg_file = f.read()
    f.closed
    cairosvg.svg2png(bytestring=svg_file,write_to=fout)
    fout.close()