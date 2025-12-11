#Nama : Muhammad Aditya Putra
#NIM  : D0425516
#Prodi : Sistem Informasi

#algoritma bubble sorting
def bubble_sort(arr):
    """Mengurutkan list menggunakan algoritma Bubble Sort."""
    n = len(arr)

    # Iterasi melalui semua elemen array
    for i in range(n):
        # Perbandingan dilakukan hanya pada sisa elemen yang belum terurut
        # n-i-1 karena i elemen terakhir sudah berada di posisi yang benar
        for j in range(0, n - i - 1):
            
            # Bandingkan elemen yang berdekatan
            if arr[j] > arr[j + 1]:
                # Jika elemen kiri lebih besar dari elemen kanan, tukar (swap)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

print("--- 1. Bubble Sort ---")
data_bubble = [64, 34, 25, 12, 22, 11, 90]
print(f"Data Awal: {data_bubble}")

sorted_bubble = bubble_sort(data_bubble.copy())
print(f"Data Terurut: {sorted_bubble}")
print("-" * 30)

#algoritma selection sorting
def selection_sort(arr):
    """Mengurutkan list menggunakan algoritma Selection Sort."""
    n = len(arr)

    # Iterasi dari elemen pertama hingga elemen kedua terakhir
    for i in range(n):
        # Asumsikan elemen saat ini (i) adalah elemen minimum
        min_idx = i

        # Cari elemen minimum di sisa list yang belum terurut (i+1 sampai n)
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j # Perbarui indeks minimum

        # Tukar (swap) elemen minimum yang ditemukan dengan elemen pada posisi i
        # Ini menempatkan elemen terkecil ke posisi yang benar
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

print("--- 2. Selection Sort ---")
data_selection = [64, 34, 25, 12, 22, 11, 90]
print(f"Data Awal: {data_selection}")

sorted_selection = selection_sort(data_selection.copy())
print(f"Data Terurut: {sorted_selection}")
print("-" * 30)

#algoritma insertion sorting 
def insertion_sort(arr):
    """Mengurutkan list menggunakan algoritma Insertion Sort."""
    n = len(arr)

    # Iterasi mulai dari elemen kedua (indeks 1) hingga akhir
    for i in range(1, n):
        key = arr[i] # Ambil elemen yang akan dimasukkan ke bagian terurut
        j = i - 1    # Indeks elemen terakhir dari bagian yang sudah terurut

        # Pindahkan elemen-elemen dari arr[0..i-1] yang lebih besar dari key,
        # ke satu posisi di depan posisi mereka saat ini
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Sisipkan key ke posisi yang benar
        arr[j + 1] = key
        
    return arr

print("--- 3. Insertion Sort ---")
data_insertion = [64, 34, 25, 12, 22, 11, 90]
print(f"Data Awal: {data_insertion}")

sorted_insertion = insertion_sort(data_insertion.copy())
print(f"Data Terurut: {sorted_insertion}")
print("-" * 30)
