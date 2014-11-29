import argparse 
import random
import sys
import svgwrite
import cairosvg
from circle import Circle

class Splash(object):
    def __init__(self):
        self.colors = ['#4d4d4d','#0000ff','#0066ff']
        self.c = random.randint(0, 2)
        self.cx =random.randint(-200, 1000)
        self.cy = random.randint(-200, 800)
        self.r = random.randint(1, 50)
        self.direction = random.randint(0, 360)
        self.splashes = random.randint(5, 15)

    def define (self, 
            dwg, 
            stroke=None, 
            fill=None,
            cx=None, 
            cy=None,
            r=None,
            direction=None,
            splashes=None):
        stroke = stroke or self.colors[self.c]
        fill = fill or stroke
        cx = cx or self.cx
        cy = cy or self.cy
        r = r or self.r
        direction = direction or self.direction
        splashes = splashes or self.splashes

        for splash in range(0,splashes):
            _cx = random.randint(r, r + int(r*0.5))
            _cx = cx + _cx*random.uniform(-1, 1)
            _cy = random.randint(r, r + int(r*0.5))
            _cy = cy + _cy*random.uniform(-1, 1)
            _r = random.randint(int(r*0.2), int(r*0.5))
            circle = Circle()
            circle.define(dwg, stroke=stroke, cx=_cx, cy=_cy, r=_r)

        return dwg.add(dwg.circle(
            (cx, cy), 
            r,
            stroke=stroke,
            fill=fill))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-svg", type=str, help="svg file name", default="splash")
    parser.add_argument("-png", type=str, help="png file name", default="splash")
    parser.add_argument("-w", type=int, help="Image width", default=400)
    parser.add_argument("-he", type=int, help="Image height", default=300)
    args = parser.parse_args()
    svg = '%s.svg' % (args.svg)
    png = '%s.png' % (args.png)
    w = '%ipx' % (args.w)
    h = '%ipx' % (args.he)
    dwg = svgwrite.Drawing(filename = svg, size = (w, h))
    splash = Splash()
    splash.define(dwg, cx=200, cy=150, r=50)
    dwg.save()
    fout = open(png,'w')
    with open(svg, 'r') as f:
        svg_file = f.read()
    f.closed
    cairosvg.svg2png(bytestring=svg_file,write_to=fout)
    fout.close()