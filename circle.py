import random
import sys
import svgwrite
import cairosvg

class Circle(object):
    def __init__(self):
        self.colors = ['#4d4d4d','#0000ff','#0066ff']
        self.c = random.randint(0, 2)
        self.xc =random.randint(0, 800)
        self.yc = random.randint(0, 600)
        self.r = random.randint(1, 500)

    def define (self, 
            dwg, 
            color=None, 
            xc=None, 
            yc=None,
            r=None):
        color = color or self.colors[self.c]
        xc = xc or self.xc
        yc = yc or self.yc
        r = r or self.r

        return dwg.add(dwg.circle(
            (xc, yc), 
            r,
            stroke=color,
            fill=color))

if __name__ == "__main__":
    svg = 'circle.svg'
    png = 'circle.png'
    if len(sys.argv) > 1:
        svg = sys.argv[1]
        if len(sys.argv) > 2:
            png = sys.argv[2]
    dwg = svgwrite.Drawing(filename = svg, size = ("800px", "600px"))
    circle = Circle()
    circle.define(dwg)
    dwg.save()
    fout = open(png,'w')
    with open(svg, 'r') as f:
        svg_file = f.read()
    f.closed
    cairosvg.svg2png(bytestring=svg_file,write_to=fout)
    fout.close()