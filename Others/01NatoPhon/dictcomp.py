from random import randint

students = []

std_scr = {each : randint(1,6) for each in students}

examine = {key : "best" for (key , value) in std_scr.items() if value == 1}

print(examine)