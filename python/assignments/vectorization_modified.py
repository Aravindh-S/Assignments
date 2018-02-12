import math
from math import sqrt

import cv2
import numpy as np
from numpy.linalg import norm
from PIL import Image
from matplotlib.colors import LinearSegmentedColormap

import time
start_time = time.time()


def synthesize_background(bg_size, colors, points):
    width, height = bg_size
    im = Image.new('RGB', (width, height))
    ld = im.load()
    heatmap = [(clr[0] / 255.0, clr[1] / 255.0, clr[2] / 255.0) for clr in colors]

    points = np.array(points)
    clr1_x, clr1_y = points[0]
    clr2_x, clr2_y = points[1]
    clr3_x, clr3_y = points[2]

    x = np.arange(0, 1000, 1)
    y = np.arange(0, 1000, 1)

    d1x = (clr1_x - x) ** 2
    d1y = (clr1_y - y) ** 2
    xs1, ys1 = np.meshgrid(d1x, d1y)
    z1 = 1 / (np.sqrt(xs1 + ys1) + 0.000000001)

    d2x = (clr2_x - x) ** 2
    d2y = (clr2_y - y) ** 2
    xs2, ys2 = np.meshgrid(d2x, d2y)
    z2 = 1 / (np.sqrt(xs2 + ys2) + 0.000000001)

    d3x = (clr3_x - x) ** 2
    d3y = (clr3_y - y) ** 2
    xs3, ys3 = np.meshgrid(d3x, d3y)
    z3 = 1 / (np.sqrt(xs3 + ys3) + 0.000000001)

    max_dist = z1 + z2 + z3
    z1 = z1 / max_dist
    z2 = z2 / max_dist
    z3 = z3 / max_dist

    clr1_rgb = heatmap[0]
    clr2_rgb = heatmap[1]
    clr3_rgb = heatmap[2]

    # Calculate color of current pixel combining all 3 colors
    # with their corresponding weights
    r, g, b = map(lambda x, y, z: x + y + z,
                  map(lambda a: a * z1, clr1_rgb),
                  map(lambda b: b * z2, clr2_rgb),
                  map(lambda c: c * z3, clr3_rgb))

    r = np.round(r * 255)
    g = np.round(g * 255)
    b = np.round(b * 255)

    for i in range(1000):
        for j in range(1000):
            ld[j, i] = int(r[i][j]), int(g[i][j]), int(b[i][j])

    im = np.array(im, np.uint8)
    return im
    '''
    x1sq = np.array((x - clr1_x)**2)
    x2sq = np.array((x - clr2_x)**2)
    x3sq = np.array((x - clr3_x)**2)
    y1sq = np.array((y - clr1_y)**2)
    y2sq = np.array((y - clr2_y)**2)
    y3sq = np.array((y - clr3_y)**2)
    '''


if __name__ == '__main__':

    CLRS = [[136, 150, 157], [153, 119, 81], [225, 185, 93]]
    PTS = [[200, 150], [991, 200], [530, 840]]
    BG_SIZE = (1000, 1000)
    im = synthesize_background(BG_SIZE, CLRS, PTS)
    im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)

    cv2.imshow('t', im)
    print("--- %s seconds ---" % (time.time() - start_time))
    cv2.waitKey()
