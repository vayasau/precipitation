# tikrina ar sekamoje teritorijoje yra krituliu

import numpy as np
from PIL import Image
from color_plte import color_plte

def warning_flag(warn_area, map_image):
    precipitation = color_plte()

    # sekamos zonos koordinates i masyva
    warn_a = np.array(warn_area)
    # grupuoja x ir y koordinates i atskirus masyvus
    warn_a_conv = np.array_split(warn_a, 2, axis=1)  # eilute (y koordinate): newarr[0], stulpelis (x koordinate): newarr[1]
    # paveikslas i masyva
    with Image.open(map_image) as im:
        map_a = np.asarray(im)

        # testavimui, sekama zona zemelapyje nudazo juodai
        # for c in warn_area:
        #     m = map_a[c[1],c[0]]=0
        # new_im = Image.fromarray(map_a)
        # new_im.show()

    # gaunamos sekamos zonos reiksmes zemelapio paveiksle
    values_on_map = map_a[(warn_a_conv[1]), (warn_a_conv[0])]
    # tikrinama ar krituliu reiksmes yra sekamoje zonoje
    check = any(item in precipitation for item in values_on_map)
    if check:
        return 1  # jei True
    else:
        return 0  # jei False
