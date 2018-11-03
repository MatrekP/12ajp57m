# Domácí úkol 1 - zobrazení
Marek Popp

2018-11-03 

Klášter u Nepomuka

## Popis programu
Program počítá polohu jednotlivých poledníků a rovnoběžek pro vybrané měřítko, poloměr referenční koule a zvolené tečné válcové zobrazení (Marinovo, Lambertovo, Braunovo či Mercatorovo). Rovnoběžky i poledníky se vypočítávají po 10 stupních.
Program počítá souřadnice bodů určných zeměpisnou délkou a šířkou.

## Vstup
Uživatel vybere `zobrazení` zadáním jednoho písmena z následujících možností:
- `A` - Marinovo zobrazení 
- `L` - Lambertovo zobrazení
- `B` - Braunovo zobrazení 
- `M` - Mercatorovo zobrazení 
Dále uživatel zadá měřítkové číslo `m` (přirozené číslo) a poloměr referenční koule Země `r` v km (kladné reálné číslo). Pokud uživatel zadá poloměr 0, bude počítáno s poloměrem 6371,11 km.

Program se po vypsání souřadnic rovnoběžek a poledníků zeptá na zeměpisnou šířku a délku ve stupních pro výpočet souřadnice bodu.
Zadáním zeměpisné šířky `0` a zeměpisné délky `0` program skončí.

## Výstup
Program pro korektní vstup vypíše vypočtené souřadnice rovnoběžek a poledníků v cm s přesností na desetiny pro zadané zobrazení, měřítko a poloměr referenční koule. 
Pokud některá vzdálenost od souřadnice (0, 0) překročí 1 m, program vypíše `-`.

## Popis činnosti programu
Program se zeptá uživatele na jedno ze zobrazení, měřítkové číslo a polomer referencni koule a ověří správnost vstupu. Pokud uživatel zadá korektní vstup, program vypočítá a vypíše souřadnice rovnoběžek a poledníků na svislé, resp. vodorovné ose. V opačném případě program napíše chybovou hlášku a skončí.
Program se dále zeptá na zeměpisnou šířku a délku bodu a vypočte jeho přepočtené souřadnice. Pokud uživatel zadá špatné souřadnice bodu, program napíše chybovou hlášku a čeká na opravu.

### Příklad běhu programu
```
Zadej zobrazeni: M
Zadej meritkove cislo: 50000000
Zadej polomer Zeme: 0
Rovnobezky: - -31.0 -22.1 -16.8 -12.9 -9.7 -7.0 -4.5 -2.2 0.0 2.2 4.5 7.0 9.7 12.9 16.8 22.1 31.0 - 
Poledniky: -40.0 -37.8 -35.6 -33.4 -31.1 -28.9 -26.7 -24.5 -22.2 -20.0 -17.8 -15.6 -13.3 -11.1 -8.9 -6.7 -4.4 -2.2 0.0 2.2 4.4 6.7 8.9 11.1 13.3 15.6 17.8 20.0 22.2 24.5 26.7 28.9 31.1 33.4 35.6 37.8 40.0 
Zadej zemepisnou sirku: 60
Zadej zemepisnou delku: -40
x  16.8
y  -8.9
Zadej zemepisnou sirku: 0
Zadej zemepisnou delku: 0
x  0.0
y  0.0
```

### Chybové hlášky
`CHYBNY VSTUP !!!` - uživatel zadal nepodporované zobrazení, měřítkové číslo či poloměr Země.
`CHYBNA ZEMEPISNA SOURADNICE !!!` - uživatel zadal nekorektní vstup pro výpočet souřadnic bodu 
