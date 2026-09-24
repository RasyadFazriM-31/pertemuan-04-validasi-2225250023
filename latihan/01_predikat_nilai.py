# Latihan 1: Predikat Nilai
# Input : satu nilai akhir (0-100)
# Aturan: A >= 85, B >= 70, C >= 60, D >= 50, E < 50
# Output: predikat A sampai E
nilai = float(input("Nilai akhir (0-100): "))
if nilai >= 85:
    predikat = "A"
elif nilai >= 70:
    predikat = "B"
elif nilai >= 60:
    predikat = "C"
elif nilai >= 50:
    predikat = "D"
else:
    predikat = "E"
print(f"Nilai {nilai:.2f} memperoleh predikat {predikat}.")
