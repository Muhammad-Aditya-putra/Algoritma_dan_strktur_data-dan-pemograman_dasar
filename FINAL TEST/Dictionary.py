#Nama : Muhammad Aditya Putra
#NIM : D0425516
#Prodi : Sistem Informasi

#1. Membuat Dictionary (Mahasiswa)
# Kunci: String (misalnya "NIM"), Nilai: Berbagai Tipe Data
mahasiswa = {
    "NIM": "D0425516",
    "Nama": "Muhammad Aditya Putra",
    "Prodi": "Sistem Informasi",
    "Semester": 1,
}

print("--- 1. Membuat dan Mengakses Dictionary ---")
print(f"Dictionary Mahasiswa: {mahasiswa}")

# Mengakses nilai menggunakan kunci (key)
print(f"Nama Mahasiswa: {mahasiswa['Nama']}")
print(f"Program Studi: {mahasiswa['Prodi']}")

# Menggunakan metode .get() untuk akses yang lebih aman (tidak error jika kunci tidak ada)
umur = mahasiswa.get("Umur", "Kunci 'Umur' tidak ada")
print(f"Akses Kunci yang tidak ada: {umur}")
