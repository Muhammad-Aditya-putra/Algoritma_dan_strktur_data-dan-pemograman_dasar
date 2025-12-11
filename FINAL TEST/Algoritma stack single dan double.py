#Nama : Muhammad Aditya Putra
#NIM : D0425516
#Prodi : Sistem Informasi

#Algoritma stack single dan double

#algoritma stack single

stack = []

# PUSH (menambah data)
stack.append("aditya")
stack.append("sistem informasi")

# POP (mengambil data)
hasil = stack.pop()

print("Yang diambil:", hasil)
print("Sisa stack:", stack)

#algoritma stack double

stack1 = []
stack2 = []

# Operasi pada Stack 1
stack1.append("aditys")
stack1.append("teknik")
stack1.pop()

# Operasi pada Stack 2
stack2.append("sistem informasi")
stack2.pop()

print("nama :", stack1)
print("fakultas :", stack2)
