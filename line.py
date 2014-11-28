import random
import sys
import svgwrite
import cairosvg

class Line(object):
    def __init__(self):
        self.colors = ['#4d4d4d','#0000ff','#0066ff']
        self.c = random.randint(0, 2)
        self.xi =random.randint(0, 800)
        self.xo =random.randint(0, 800)
        self.yi = random.randint(0, 600)
        self.yo = random.randint(0, 600)
        self.s = random.randint(1, 20)

    def define (self, 
            dwg, 
            color=None, 
            xi=None, 
            xo=None, 
            yi=None,
            yo=None,
            s=None):
        color = color or self.colors[self.c]
        xi = xi or self.xi
        xo = xo or self.xo
        yi = yi or self.yi
        yo = yo or self.yo
        s = s or self.s

        return dwg.add(dwg.line(
            (xi, yi), 
            (xo, yo), 
            stroke_width=s,
            stroke_linecap="round",
            stroke=color))

if __name__ == "__main__":
    svg = 'line.svg'
    png = 'line.png'
    if len(sys.argv) > 1:
        svg = sys.argv[1]
        if len(sys.argv) > 2:
            png = sys.argv[2]
    dwg = svgwrite.Drawing(filename = svg, size = ("800px", "600px"))
    line = Line()
    line.define(dwg)
    dwg.save()
    fout = open(png,'w')
    with open(svg, 'r') as f:
        svg_file = f.read()
    f.closed
    cairosvg.svg2png(bytestring=svg_file,write_to=fout)
    fout.close()