import random
cena_paliwa = float(input("Podaj cenę paliwa w zł:"))
droga = int(random.randint(1,500))
spalanie = float (input("Podaj średnie spalanie w litrach na 100km: "))

zuycie_paliwa = droga *(spalanie / 100)
koszty = zuycie_paliwa * cena_paliwa

print("Samochód spali:", round(zuycie_paliwa, 2), "litrów")
print("Koszty wynoszą:", round(koszty), "zł", "na trasie", droga, "km")

