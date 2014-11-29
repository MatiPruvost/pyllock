import random
import sys
import svgwrite
import cairosvg

class Parabola(object):
    def __init__(self):
        self.colors = ['#4d4d4d','#0000ff','#0066ff']
        self.c = random.randint(0, 2)
        self.x1 =random.randint(0, 800)
        self.x2 =random.randint(0, 800)
        self.y1 = random.randint(0, 600)
        self.y2 = random.randint(0, 600)
        self.qx = str(random.randint(0, 200))
        self.qy = str(random.randint(0, 200))
        self.stroke_width = random.randint(1, 20)
        self.stroke_linecap = "round"
        self.stroke_width = random.randint(1, 20)
        self.fill = "none"

    def define (self, 
            dwg, 
            color=None, 
            x1=None, 
            x2=None, 
            y1=None,
            y2=None,
            qx=None,
            qy=None,
            stroke_linecap=None,
            stroke_width=None,
            fill=None):
        color = color or self.colors[self.c]
        x1 = x1 or self.x1
        x2 = x2 or self.x2
        y1 = y1 or self.y1
        y2 = y2 or self.y2
        qx = qx or self.qx
        qy = qy or self.qy
        stroke_width = stroke_width or self.stroke_width
        stroke_linecap = stroke_linecap or self.stroke_linecap
        fill = fill or self.fill
        d = ["M", x1, y1, "q", qx, qy, x2, y2]
        d = [str(element) for element in d]
        d = " ".join(d)

        return dwg.add(dwg.path(d=d,
                stroke=color,
                stroke_width=stroke_width,
                stroke_linecap=stroke_linecap,
                fill=fill,
            ))


if __name__ == "__main__":
    svg = 'parabola.svg'
    png = 'parabola.png'
    if len(sys.argv) > 1:
        svg = sys.argv[1]
        if len(sys.argv) > 2:
            png = sys.argv[2]
    dwg = svgwrite.Drawing(filename = svg, size = ("800px", "600px"))
    parabola = Parabola()
    parabola.define(dwg)
    dwg.save()
    fout = open(png,'w')
    with open(svg, 'r') as f:
        svg_file = f.read()
    f.closed
    cairosvg.svg2png(bytestring=svg_file,write_to=fout)
    fout.close()