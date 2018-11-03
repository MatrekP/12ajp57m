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
    print("Polomer Zeme je nyni kladny !!!")

u = -90         # zem. sirka
v = -180        # zem. delka


""" deklarace funkci """
def marinus(r, u, m):
    return 100000 * r * radians(u) / m

def lambert(r, u, m):
    return 100000 * r * sin(radians(u)) / m

def braun(r, u, m):
    return 100000 * 2 * r * tan(radians(u) / 2) / m

def mercator(r, u, m):
    if u == -90 or u == 90:
        return "-"
    return 100000 * r * log(1 / (tan(radians(u + 90) / 2)), e) / m

def poledniky(r, v, m):
    return 100000 * r * radians(v) / m


""" rovnobezky """
if zobrazeni == "A" or zobrazeni == "a":
    """ Marinovo zobrazeni """
    print("Rovnobezky: ", end="")
    while u <= 90:
        y = marinus(r, u, m)
        u = u + 10
        if y < -100 or y > 100:
            print("-", end=" ")
        else:
            print(round(y, 1), end=" ")
elif zobrazeni == "L" or zobrazeni == "l":
    """ Lambertovo zobrazeni """
    print("Rovnobezky: ", end="")
    while u <= 90:
        y = lambert(r, u, m)
        u = u + 10
        if y < -100 or y > 100:
            print("-", end=" ")
        else:
            print(round(y, 1), end=" ")
elif zobrazeni == "B" or zobrazeni == "b":
    """ Braunovo zobrazeni """
    print("Rovnobezky: ", end="")
    while u <= 90:
        y = braun(r, u, m)
        u = u + 10
        if y < -100 or y > 100:
            print("-", end=" ")
        else:
            print(round(y, 1), end=" ")
elif zobrazeni == "M" or zobrazeni == "m":
    """ Mercatorovo zobrazeni """
    print("Rovnobezky: ", end="")
    while u <= 90:
        y = mercator(r, -u, m)
        u = u + 10
#        if y < -100 or y > 100:            #TypeError: '<' not supported between instances of 'str' and 'int'
#            print("-", end=" ")
        if y == "-":
            print(y, end=" ")
        else:
            print(round(y, 1), end=" ")
else:
    print("Chybne zobrazeni !!!")
print()


""" poledniky """
if zobrazeni == "A" or zobrazeni == "a" or zobrazeni == "L" or zobrazeni == "l" or zobrazeni == "B" or zobrazeni == "b" or zobrazeni == "M" or zobrazeni == "m":
    print("Poledniky: ", end="")
    while v <= 180:
        x = poledniky(r, v, m)
        v = v + 10
        if x < -100 or x > 100:
            print("-", end=" ")
        else:
            print(round(x, 1), end=" ")
