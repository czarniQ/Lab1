cena_paliwa = 6.50
droga = int(input("Podaj pokonaną drogę w km:"))
spalanie = float (input("Podaj średnie spalanie w litrach na 100 km"))

print (f"Zużycie paliwa przy {droga} km wyniesie ok. {round((spalanie / 100) * droga , 2)} ")
print (f"Koszt przy {droga} km wyniesie ok. {round(((spalanie / 100) * droga) * cena_paliwa , 2)} zł.")