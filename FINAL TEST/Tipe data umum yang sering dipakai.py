#Nama : Muhammad Aditya Putra
#NIM : D0425516
#Prodi : Sistem Informasi

#integer
umur = 19
jumlah_siswa = 30
tahun_lahir = -2005

print("--- 1. Tipe Data INTEGER ---")
print(f"Nilai umur: {umur}, Tipe: {type(umur)}")
print(f"Nilai jumlah_siswa: {jumlah_siswa}, Tipe: {type(jumlah_siswa)}")

# --- Operasi pada Integer ---
penambahan = umur + 5
pengurangan = jumlah_siswa - 50
perkalian = umur * 2

print(f"Penambahan (25 + 5): {penambahan}")
print(f"Perkalian (25 * 2): {perkalian}")

#Float
suhu = 36.5
pi = 3.14159
harga_per_unit = 15000.50

print("\n--- 2. Tipe Data FLOAT ---")
print(f"Nilai suhu: {suhu}, Tipe: {type(suhu)}")
print(f"Nilai pi: {pi}, Tipe: {type(pi)}")

# --- Operasi pada Float ---
luas_lingkaran = pi * (7 ** 2)
pembagian = 100 / 3

print(f"Luas lingkaran (dengan float pi): {luas_lingkaran}")
print(f"Hasil pembagian (100 / 3): {pembagian}")

#String
nama = "Muhammad Aditya Putra"
pesan = 'Selamat datang di kelas pemrograman.'
nomor_telepon_str = "0812345678" # Angka yang diperlakukan sebagai teks

print("\n--- 3. Tipe Data STRING ---")
print(f"Nilai nama: {nama}, Tipe: {type(nama)}")
print(f"Nilai pesan: {pesan}, Tipe: {type(pesan)}")

# --- Operasi pada String ---

# A. Penggabungan (Concatenation)
sapaan = "Halo, " + nama
print(f"Penggabungan String: {sapaan}")

# B. Panjang String (Length)
panjang_nama = len(nama)
print(f"Panjang nama '{nama}': {panjang_nama} karakter")

# C. Mengakses Karakter (Indeks dimulai dari 0)
huruf_pertama = nama[0]
print(f"Karakter pertama dari nama: {huruf_pertama}")
