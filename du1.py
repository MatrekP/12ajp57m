from math import radians, sin, tan, log, e

# funkce
# pro jednotliva tecna valcova zobrazeni
def rovnobezky(r, u, m):
    if zobrazeni == "A":            # Marinovo zobrazeni
        return 100000 * r * radians(u) / m
    elif zobrazeni == "L":          # Lambertovo zobrazeni
        return 100000 * r * sin(radians(u)) / m
    elif zobrazeni == "B":          # Braunovo zobrazeni
        return 100000 * 2 * r * tan(radians(u) / 2) / m
    elif zobrazeni == "M":          # Mercatorovo zobrazeni
        if u == -90 or u == 90:
            return "-"
        else:
            return 100000 * r * log(1 / (tan(radians(u + 90) / 2)), e) / m


# funkce pocitajici polohu poledniku
# pocitano pro vsechna zobrazeni stejne
def poledniky(r, v, m):
    return 100000 * r * radians(v) / m


# zadani vstupu
zobrazeni = input("Zadej zobrazeni: ")
m = int(input("Zadej meritkove cislo: "))
r = float(input("Zadej polomer Zeme: "))
if r == 0:
    r = 6371.11


# deklarace promennych pro vzorce zobrazeni
u = -90         # zem. sirka
v = -180        # zem. delka


# zjisteni spravnosti vstupu a vypis vypoctu zobrazeni
if m > 0 and r > 0 and zobrazeni in ("A", "L", "B", "M"):
    print("Rovnobezky:", end=" ")
    for i in range(-90, 100, 10):
        y = rovnobezky(r, u, m)
        u = u + 10
        if y == "-":
            print(y, end=" ")
        elif y < -100 or y > 100:
            print("-", end=" ")
        else:
            print(round(y, 1), end=" ")
    print()
    print("Poledniky:", end=" ")
    for i in range(-180, 190, 10):
        x = poledniky(r, v, m)
        v = v + 10
        if x < -100 or x > 100:
            print("-", end=" ")
        else:
            print(round(x, 1), end=" ")
else:
    print("Chybny vstup !!!")
