# Pertemuan 04 - Seleksi Multi-Kondisi dan Validasi Input

Nama: Rasyad Fazri Mulyono  
NIM: 2225250023  
Kelas: 3A

## Tujuan

Membangun program validasi dan klasifikasi dengan rantai if-elif-else, meliputi validasi tipe, rentang, dan domain, serta menggabungkannya dalam satu alur program yang runtut.

## Cara Menjalankan

```bash
python3 praktik/validasi_klasifikasi_nilai.py
```

## Tabel Keputusan

Program membaca nilai ujian, nilai tugas, dan kehadiran (persen), lalu menentukan nilai akhir, predikat, dan status.

| No | Cabang | Syarat Kode | Contoh Masukan | Keluaran Diharapkan |
|:---|:---|:---|:---|:---|
| 1 | Penolakan tipe | konversi float gagal (ValueError) | ujian = "abc" | Masukan ditolak: seluruh data harus berupa angka. |
| 2 | Penolakan rentang ujian | not (0 <= ujian <= 100) | ujian = 105 | Masukan ditolak: nilai ujian di luar rentang 0 sampai 100. |
| 3 | Penolakan rentang tugas | not (0 <= tugas <= 100) | tugas = -5 | Masukan ditolak: nilai tugas di luar rentang 0 sampai 100. |
| 4 | Penolakan rentang kehadiran | not (0 <= hadir <= 100) | hadir = 120 | Masukan ditolak: kehadiran di luar rentang 0 sampai 100. |
| 5 | Tidak memenuhi syarat kehadiran | hadir < 80 | 90, 90, 75 | Nilai akhir tampil, Status: Tidak memenuhi syarat kehadiran. |
| 6 | Predikat A | akhir >= 85 | 90, 80, 95 | Nilai akhir = 86.00, Predikat A, Lulus |
| 7 | Predikat B | akhir >= 70 | 75, 70, 85 | Nilai akhir = 73.00, Predikat B, Lulus |
| 8 | Predikat C | akhir >= 60 | 60, 60, 80 | Nilai akhir = 60.00, Predikat C, Lulus |
| 9 | Predikat D | akhir >= 50 | 55, 50, 90 | Nilai akhir = 53.00, Predikat D, Belum lulus |
| 10 | Predikat E | selain di atas (cabang else) | 40, 30, 100 | Nilai akhir = 36.00, Predikat E, Belum lulus |

Keterangan: nilai akhir = 0.6 x nilai ujian + 0.4 x nilai tugas. Status Lulus untuk predikat A, B, C; Belum lulus untuk predikat D, E.

## Hasil Pengujian

### Latihan 1 - Predikat Nilai (01_predikat_nilai.py)

| Masukan | Keluaran Diharapkan | Keluaran Aktual | Status |
|:---|:---|:---|:---|
| 92 | Predikat A | Nilai 92.00 memperoleh predikat A. | sesuai |
| 85 | Predikat A | Nilai 85.00 memperoleh predikat A. | sesuai |
| 84.9 | Predikat B | Nilai 84.90 memperoleh predikat B. | sesuai |
| 70 | Predikat B | Nilai 70.00 memperoleh predikat B. | sesuai |
| 60 | Predikat C | Nilai 60.00 memperoleh predikat C. | sesuai |
| 50 | Predikat D | Nilai 50.00 memperoleh predikat D. | sesuai |
| 49.9 | Predikat E | Nilai 49.90 memperoleh predikat E. | sesuai |

### Latihan 2 - Kategori Bilangan (02_kategori_bilangan.py)

| Masukan | Keluaran Diharapkan | Keluaran Aktual | Status |
|:---|:---|:---|:---|
| -7 | Bilangan negatif | Bilangan negatif | sesuai |
| 0 | Nol | Nol | sesuai |
| 8 | Bilangan positif genap | Bilangan positif genap | sesuai |
| 13 | Bilangan positif ganjil | Bilangan positif ganjil | sesuai |

### Latihan 3 - Validasi Rentang (03_validasi_rentang.py)

| Masukan | Keluaran Diharapkan | Keluaran Aktual | Status |
|:---|:---|:---|:---|
| 45 | Sudut lancip | Sudut lancip | sesuai |
| 90 | Sudut siku-siku | Sudut siku-siku | sesuai |
| 135 | Sudut tumpul | Sudut tumpul | sesuai |
| 0 | Pesan penolakan | Masukan ditolak: sudut harus lebih dari 0 dan kurang dari 180. | sesuai |
| 180 | Pesan penolakan | Masukan ditolak: sudut harus lebih dari 0 dan kurang dari 180. | sesuai |
| -30 | Pesan penolakan | Masukan ditolak: sudut harus lebih dari 0 dan kurang dari 180. | sesuai |

### Latihan 4 - Validasi Tipe (04_validasi_tipe.py)

| Masukan | Keluaran Diharapkan | Keluaran Aktual | Status |
|:---|:---|:---|:---|
| 15 | 75.00 persen, Tuntas | Persentase = 75.00 persen, Tuntas | sesuai |
| 14 | 70.00 persen, Belum tuntas | Persentase = 70.00 persen, Belum tuntas | sesuai |
| 20 | 100.00 persen, Tuntas | Persentase = 100.00 persen, Tuntas | sesuai |
| 0 | 0.00 persen, Belum tuntas | Persentase = 0.00 persen, Belum tuntas | sesuai |
| 21 | Pesan penolakan rentang | Masukan ditolak: jumlah harus berada pada rentang 0 sampai 20. | sesuai |
| dua belas | Pesan penolakan tipe | Masukan ditolak: jumlah harus berupa bilangan bulat. | sesuai |

### Latihan 5 - Klasifikasi Segitiga Berdasarkan Sudut (05_klasifikasi_segitiga_sudut.py)

| Masukan (a, b, c) | Keluaran Diharapkan | Keluaran Aktual | Status |
|:---|:---|:---|:---|
| 60, 60, 60 | Segitiga lancip | Segitiga lancip | sesuai |
| 90, 45, 45 | Segitiga siku-siku | Segitiga siku-siku | sesuai |
| 120, 30, 30 | Segitiga tumpul | Segitiga tumpul | sesuai |
| 100, 50, 40 | Pesan penolakan jumlah sudut | Masukan ditolak: jumlah ketiga sudut harus 180 derajat. | sesuai |
| 0, 90, 90 | Pesan penolakan sudut positif | Masukan ditolak: setiap sudut harus lebih dari 0 derajat. | sesuai |

### Praktik 1 - Validasi dan Klasifikasi Nilai (praktik/validasi_klasifikasi_nilai.py)

| Ujian | Tugas | Kehadiran | Keluaran Diharapkan | Keluaran Aktual | Status |
|:---|:---|:---|:---|:---|:---|
| 90 | 80 | 95 | Nilai akhir 86.00, Predikat A, Lulus | Nilai akhir = 86.00, Predikat: A, Status: Lulus | sesuai |
| 75 | 70 | 85 | Nilai akhir 73.00, Predikat B, Lulus | Nilai akhir = 73.00, Predikat: B, Status: Lulus | sesuai |
| 60 | 60 | 80 | Nilai akhir 60.00, Predikat C, Lulus | Nilai akhir = 60.00, Predikat: C, Status: Lulus | sesuai |
| 55 | 50 | 90 | Nilai akhir 53.00, Predikat D, Belum lulus | Nilai akhir = 53.00, Predikat: D, Status: Belum lulus | sesuai |
| 40 | 30 | 100 | Nilai akhir 36.00, Predikat E, Belum lulus | Nilai akhir = 36.00, Predikat: E, Status: Belum lulus | sesuai |
| 90 | 90 | 75 | Nilai akhir 90.00, Tidak memenuhi syarat kehadiran | Nilai akhir = 90.00, Status: Tidak memenuhi syarat kehadiran. | sesuai |
| 105 | 80 | 90 | Pesan penolakan rentang nilai ujian | Masukan ditolak: nilai ujian di luar rentang 0 sampai 100. | sesuai |
| 80 | -5 | 90 | Pesan penolakan rentang nilai tugas | Masukan ditolak: nilai tugas di luar rentang 0 sampai 100. | sesuai |
| 80 | 80 | abc | Pesan penolakan tipe | Masukan ditolak: seluruh data harus berupa angka. | sesuai |

## Refleksi

Satu masukan tidak valid yang semula terlewat adalah **kehadiran dengan nilai di atas 100**, misalnya 120. Pada awalnya validasi rentang hanya terpikir untuk nilai ujian dan nilai tugas, padahal kehadiran juga dinyatakan dalam persen sehingga wajib berada pada rentang 0 sampai 100. Setelah menyusun tabel keputusan, barulah terlihat bahwa butir penolakan rentang kehadiran adalah cabang tersendiri yang harus diuji. Pelajaran yang didapat: menyusun tabel keputusan sebelum menulis kode memastikan seluruh cabang, termasuk cabang penolakan, teridentifikasi dan teruji.

## Struktur Berkas

```
pertemuan-04-validasi-NIM/
|-- README.md
|-- latihan/
|   |-- 01_predikat_nilai.py
|   |-- 02_kategori_bilangan.py
|   |-- 03_validasi_rentang.py
|   |-- 04_validasi_tipe.py
|   `-- 05_klasifikasi_segitiga_sudut.py
`-- praktik/
    `-- validasi_klasifikasi_nilai.py
```

## Referensi

- Bahan ajar Pertemuan 4, Algoritma dan Pemrograman, S1 Pendidikan Matematika FKIP Untirta.
- Downey, A. B. (2015). Think Python (2nd ed.). Green Tea Press.
- Python Software Foundation. Python Tutorial: Errors and Exceptions.
