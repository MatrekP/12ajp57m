from math import radians, sin, tan, log, e

""" zadani vstupu """
zobrazeni = input("Zadej zobrazeni: ")
m = int(input("Zadej meritkove cislo: "))
if m <= 0:
    print("Chybne meritkove cislo !!!")
r = float(input("Zadej polomer Zeme: "))
if r == 0:
    r = 6371.11
if r < 0:
    r = -r
    print("Polomer Zeme je nyni kladny")

u = -90             #zem. sirka
v = -180            #zem. delka

""" vypocty """
if zobrazeni == "A":
    print("Marinovo zobrazeni")
    while u <= 90:
        y = (100000 * r * radians(u)) / m
        u = u + 10
        print(y)
elif zobrazeni == "L":
    print("Lambertovo zobrazeni")
    while u <= 90:
        y = (100000 * r * sin(radians(u))) / m
        u = u + 10
        print(y)
elif zobrazeni == "B":
    print("Braunovo zobrazeni")
    while u <= 90:
        y = (100000 * 2 * r * tan(radians(u)/2)) / m
        u = u + 10
        print(y)
elif zobrazeni == "M":
    print("Mercatorovo zobrazeni")
    u = -80
    while u < 0:
        y = 100000 * r * log(1/(tan(radians(u + 90)/2)),e) / m * (-1)     # upravit
        u = u + 10
        # if y > -0.001:
        #     y = 0
        print(y)
    while u <= 80:
        y = 100000 * r * log(1/(tan(radians(90 - u)/2)),e) / m
        # y = radians(90 - u)
        # y = 1/(tan(y/2))
        # y = log(y,e)
        # y = 100000 * r * y / m
        if y < 0.001:
            y = 0
        u = u + 10
        print(y)
else:
    print("Chybny vstup !!!")
print()

if (zobrazeni == "A") or (zobrazeni == "L") or (zobrazeni == "B") or (zobrazeni == "M"):
    while v <= 180:
        x = (100000 * r * radians(v)) / m
        v = v + 10
        print(x)
