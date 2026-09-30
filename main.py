with open('cisla.txt') as soubor:
    cisla = [int(radek.strip()) for radek in soubor if radek.strip()]
if cisla:
    print(max(cisla))
else:
    print("Soubor je prázdný.")