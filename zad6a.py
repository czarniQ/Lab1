import random
cena_paliwa = float(input("Podaj cenę paliwa w zł:"))
droga = int(random.randint(1,500))
spalanie = float (input("Podaj średnie spalanie w litrach na 100km: "))

print(f"Zużycie paliwa przy {droga} km wyniesie około {round((spalanie / 100) * droga , 2)} ")
print(f"Koszt przy {droga} km wyniesie około {round(((spalanie / 100) * droga) * cena_paliwa)} ")

