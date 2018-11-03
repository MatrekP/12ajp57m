from math import radians, sin, tan, log, e


# funkce
# pro jednotliva tecna valcova zobrazeni
def rovnobezky(r, u, m):
    if zobrazeni in ("A", "a"):            # Marinovo zobrazeni
        return 100000 * r * radians(u) / m
    elif zobrazeni in ("L", "l"):          # Lambertovo zobrazeni
        return 100000 * r * sin(radians(u)) / m
    elif zobrazeni in ("B", "b"):          # Braunovo zobrazeni
        return 100000 * 2 * r * tan(radians(u) / 2) / m
    elif zobrazeni in ("M", "m"):          # Mercatorovo zobrazeni
        if u == -90 or u == 90:
            return "-"
        else:
            return 100000 * r * log(1 / (tan(radians(90 - u) / 2)), e) / m


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


# zjisteni spravnosti vstupu a vypis vypoctu zobrazeni
if m > 0 and r > 0 and zobrazeni in ("A", "a", "L", "l", "B", "b", "M", "m"):
    u = -90         # zemepisna sirka
    v = -180        # zemepisna delka
    print("Rovnobezky:", end=" ")
    for i in range(-90, 100, 10):
        y = rovnobezky(r, u, m)
        if y == "-":
            print(y, end=" ")
        elif y < -100 or y > 100:
            print("-", end=" ")
        else:
            print(round(y, 1), end=" ")
        u = u + 10
    print()
    print("Poledniky:", end=" ")
    for i in range(-180, 190, 10):
        x = poledniky(r, v, m)
        if x < -100 or x > 100:
            print("-", end=" ")
        else:
            print(round(x, 1), end=" ")
        v = v + 10
    print()

    # zadani a vypocet souradnic bodu
    bod_u = None
    bod_v = None
    while bod_u != 0 or bod_v != 0:
        bod_u = float(input("Zadej zemepisnou sirku: "))
        bod_v = float(input("Zadej zemepisnou delku: "))
        if -90 <= bod_u <= 90 and -180 <= bod_v <= 180:
            y = rovnobezky(r, bod_u, m)
            if y == "-":
                print("x ", y)
            elif y < -100 or y > 100:
                print("x ", "-")
            else:
                print("x ", round(y, 1))
            x = poledniky(r, bod_v, m)
            if x < -100 or x > 100:
                print("y ", "-")
            else:
                print("y ", round(x, 1))
        else:
            print("CHYBNA ZEMEPISNA SOURADNICE !!!")
else:
    print("CHYBNY VSTUP !!!")
