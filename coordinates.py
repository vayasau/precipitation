# keicia gps koordinates i beta.meteo.lt/?pid=radarai pikselio koordinates

# horizontalus mastelis px/deg
H_SCALE = 77.816648726
# vertikalus mastelis px/deg
V_SCALE = 135.753431545
# paveiksliuko koordinate x=0 laipsniais
X_ORIGIN = 19.9348
# paveiksliuko koordinate y=0 laipsniais
Y_ORIGIN = 57.0113


def gps_to_px(latitude, longitude):
    x = round((longitude - X_ORIGIN) * H_SCALE)
    y = round((Y_ORIGIN - latitude) * V_SCALE)
    return x, y
