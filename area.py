# gaunamos apskritimo pikseliu koordinates. 1px = ~817 m

import math
from itertools import tee


def circle(center_x, center_y, radius=5):
    circle_boundary = []
    for i in range(0, 360, 10):
        fi = i * math.pi / 180
        x = round(center_x + radius * math.cos(fi))
        y = round(center_y + radius * math.sin(fi))
        if [x, y] not in circle_boundary:
            circle_boundary.append([x, y])

    circle_boundary = (sorted(circle_boundary))

    # itertools.pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(circle_boundary)
    next(b, None)
    paired_list = list(zip(a, b))

    for item in paired_list:
        if item[0][0] == item[1][0]:  # poruojama pagal x koordinates (eilutes)
            if item[0][1] - item[1][1] < -1:  # filruojamos eilutes, kuriu y koorninatese yra tarpu
                # uzpildomos trukstamos y koordinates
                for i in range(item[0][1]+1, item[1][1]):
                    coord_y = [item[0][0], i]
                    circle_boundary.append(coord_y)
    area = sorted(circle_boundary)
    return area
