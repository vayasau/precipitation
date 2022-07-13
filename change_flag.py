# krituliu fakta pakeicia i priesinga

def flag_change(gps, flag):
    gps = str((f"{gps[0]:07.4f}", f"{gps[1]:07.4f}"))  # is int i str neprarandant '0' po kablelio
    if "'" in gps:  # pasalina atsiradusius "'"
        gps = gps.replace("'", '')

    if flag == 0:
        flag_to_change = 1
    if flag == 1:
        flag_to_change = 0

    with open('user.txt', 'r') as f:
        data = f.readlines()

    i = 0
    for line in data:
        if gps in line:  # kecia paskutini 1 i 0 ir atvirksciai
            flag_pos = line.rfind(str(flag_to_change))
            data[i] =  line[:flag_pos] + str(flag) + line[flag_pos+1:]
        i += 1

    with open('user.txt', 'w') as f:
        f.writelines(data)
