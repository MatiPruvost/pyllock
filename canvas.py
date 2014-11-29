import argparse 
import random
import sys
import svgwrite
import cairosvg
from circle import Circle
from line import Line
from parabola import Parabola
from splash import Splash

class Canvas(object):
    def define (self, dwg):

        for element in range(0,1000):
            circle = Circle()
            line = Line()
            parabola = Parabola()
            splash = Splash()
            circle.define(dwg)
            line.define(dwg)
            parabola.define(dwg)
            splash.define(dwg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-svg", type=str, help="svg file name", default="canvas")
    parser.add_argument("-png", type=str, help="png file name", default="canvas")
    parser.add_argument("-w", type=int, help="Image width", default=800)
    parser.add_argument("-he", type=int, help="Image height", default=600)
    args = parser.parse_args()
    svg = '%s.svg' % (args.svg)
    png = '%s.png' % (args.png)
    w = '%ipx' % (args.w)
    h = '%ipx' % (args.he)
    dwg = svgwrite.Drawing(filename = svg, size = (w, h))
    canvas = Canvas()
    canvas.define(dwg)
    dwg.save()
    fout = open(png,'w')
    with open(svg, 'r') as f:
        svg_file = f.read()
    f.closed
    cairosvg.svg2png(bytestring=svg_file,write_to=fout)
    fout.close()