# Nama : muh ikhsan resyah
# Nim : D0425512
# Dictionary

# contoh data senjata pada game
weapon = {
    "nama": "shadow",   # "key": "value" 
    "Damage": 120,
    "Rarity": "epic",
    "Type": "sword",
}

#menampilkan value
print(weapon["nama"])

# menambahkan data
weapon["user"] = "assasin"
print(weapon)

#mengubah data
weapon["Damage"] = 220
print(weapon)

#menghapus data 
del weapon["Rarity"]
print(weapon)

# loopingnya
for key, value in weapon.items():
    print(key, ":" , value)

# cek apakah keynya ada
if "Type" in weapon:
    print("ada")
else:
    print("tidak ada")

# cek lenghtnya
print(len(weapon))

    