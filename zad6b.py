import random

długość_drogi = random.randint (1,500)
droga = długość_drogi

Średnie_spalanie = float(input("Podaj średnie spalanie na 100km: "))
Cena_paliwa = float(input("Podaj cenę paliwa za litr: "))

zużycie_paliwa = droga * (Średnie_spalanie / 100)
koszt = zużycie_paliwa * Cena_paliwa

print(f"Przejechany dystans: {droga} km")
print(f"Samochód spalił: {zużycie_paliwa:.2f} litrów")
print(f"Koszt paliwa: {koszt:.2f} zł")