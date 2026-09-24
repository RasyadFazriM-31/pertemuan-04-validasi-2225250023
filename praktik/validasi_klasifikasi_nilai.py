# Praktik 1: Validasi dan Klasifikasi Nilai Akhir
# Mata Kuliah: Algoritma dan Pemrograman - Pertemuan 4
# Input : nilai ujian, nilai tugas, kehadiran (persen)
# Validasi: ketiganya harus angka (try-except ValueError) dan berada pada rentang 0-100
# Proses : nilai akhir = 0.6*ujian + 0.4*tugas; syarat kehadiran minimal 80 persen
# Output : nilai akhir (2 desimal), predikat A-E, status lulus/belum lulus
#          atau pesan penolakan yang spesifik

print("Validasi dan Klasifikasi Nilai Akhir")
teks_ujian = input("Nilai ujian (0-100): ").strip()
teks_tugas = input("Nilai tugas (0-100): ").strip()
teks_hadir = input("Kehadiran persen (0-100): ").strip()

try:
    ujian = float(teks_ujian)
    tugas = float(teks_tugas)
    hadir = float(teks_hadir)
except ValueError:
    print("Masukan ditolak: seluruh data harus berupa angka.")
else:
    if not (0 <= ujian <= 100):
        print("Masukan ditolak: nilai ujian di luar rentang 0 sampai 100.")
    elif not (0 <= tugas <= 100):
        print("Masukan ditolak: nilai tugas di luar rentang 0 sampai 100.")
    elif not (0 <= hadir <= 100):
        print("Masukan ditolak: kehadiran di luar rentang 0 sampai 100.")
    else:
        akhir = 0.6 * ujian + 0.4 * tugas
        print(f"Nilai akhir = {akhir:.2f}")
        if hadir < 80:
            print("Status: Tidak memenuhi syarat kehadiran.")
        else:
            if akhir >= 85:
                predikat = "A"
            elif akhir >= 70:
                predikat = "B"
            elif akhir >= 60:
                predikat = "C"
            elif akhir >= 50:
                predikat = "D"
            else:
                predikat = "E"
            if predikat in ("A", "B", "C"):
                status = "Lulus"
            else:
                status = "Belum lulus"
            print(f"Predikat: {predikat}")
            print(f"Status: {status}")
