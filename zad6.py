cena_paliwa = 6.50
droga = float(input("Podaj pokonaną drogę w km:"))
spalanie = float(input("Podaj średnie spalanie w litrach na 100 km"))

zuzycie_paliwa = (droga * spalanie /100)
koszty = (cena_paliwa * zuzycie_paliwa)

print("Zużycie paliwa wynosi:", round(zuzycie_paliwa, 2), "litry")
print("Szacowane koszty za tą drogę:", round(koszty, 2), "zł")


