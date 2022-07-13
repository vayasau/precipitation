# gaunami vartotojo duomenys

import ast

def get_user_data():
    with open('user.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            data = ast.literal_eval(line)
            yield data
