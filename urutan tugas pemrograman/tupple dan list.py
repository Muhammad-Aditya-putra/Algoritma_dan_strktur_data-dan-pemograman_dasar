# Nama : muh ikhsan resyah
# Nim : D0425512

#tuple

Warna = ("merah", "kuning", "hijau") #tuple tidak bisa di ubah
print("isi tuple: ", Warna)
print("Elemen ke-1:", Warna[0])
# warna[1] = "kuning"  # Ini akan ERROR karena tuple tidak bisa diubah


#List
Buah = ["semangka", "apel", "jeruk"] #Bisa diubah
print("Sebelum diubah:", Buah)

Buah[1] = "jeruk"     # mengubah isi
Buah.append("melon")  # menambah data

print("Setelah diubah:", Buah)