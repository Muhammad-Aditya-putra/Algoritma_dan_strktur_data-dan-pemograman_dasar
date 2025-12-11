#Nama : Muhammad Aditya Putra
#NIM : D0425516
#Prodi : Sistem Informasi

#Algoritma Pencarian BINER (Binary Search)
def binary_search(arr, target):
    """
    Mencari nilai target dalam list yang terurut menggunakan Binary Search.
    
    Argumen:
        arr (list): List data yang HARUS terurut.
        target (int/float): Nilai yang dicari.
        
    Mengembalikan:
        int: Indeks dari target jika ditemukan, atau -1 jika tidak ditemukan.
    """
    low = 0               # Indeks awal (rendah)
    high = len(arr) - 1   # Indeks akhir (tinggi)

    # Lakukan pengulangan selama rentang pencarian masih valid
    while low <= high:
        # Hitung indeks tengah (mid)
        # Menggunakan (low + high) // 2 adalah cara paling umum
        mid = (low + high) // 2

        # Kasus 1: Nilai ditemukan
        if arr[mid] == target:
            return mid
        
        # Kasus 2: Target berada di sebelah kanan (setengah atas)
        elif arr[mid] < target:
            low = mid + 1 # Geser indeks rendah ke kanan dari mid
        
        # Kasus 3: Target berada di sebelah kiri (setengah bawah)
        else: # arr[mid] > target
            high = mid - 1 # Geser indeks tinggi ke kiri dari mid
            
    return -1 # Target tidak ditemukan


# Algoritma Pencarian INTERPOLASI (Interpolation Search)
def interpolation_search(arr, target):
    """
    Mencari nilai target dalam list yang terurut menggunakan Interpolation Search.
    
    Algoritma ini ideal untuk data yang terdistribusi secara seragam.
    
    Argumen:
        arr (list): List data yang HARUS terurut.
        target (int/float): Nilai yang dicari.
        
    Mengembalikan:
        int: Indeks dari target jika ditemukan, atau -1 jika tidak ditemukan.
    """
    low = 0
    high = len(arr) - 1

    # Lakukan pengulangan selama rentang pencarian masih valid 
    # dan target berada dalam rentang nilai array saat ini
    while low <= high and arr[low] <= target <= arr[high]:

        # Pencegahan pembagian dengan nol dan kasus di mana semua elemen sama
        if arr[high] == arr[low]:
            return low if arr[low] == target else -1

        # Formula Interpolasi untuk memperkirakan posisi (pos)
        # Posisi dihitung berdasarkan perkiraan lokasi target di rentang saat ini
        pos = low + (high - low) * (target - arr[low]) // (arr[high] - arr[low])

        # Kasus 1: Nilai ditemukan
        if arr[pos] == target:
            return pos
        
        # Kasus 2: Target berada di sebelah kanan dari posisi yang diperkirakan
        elif arr[pos] < target:
            low = pos + 1
            
        # Kasus 3: Target berada di sebelah kiri dari posisi yang diperkirakan
        else: # arr[pos] > target
            high = pos - 1
            
    return -1 # Target tidak ditemukan

# ============================================
# Demo Penggunaan
# ============================================
# List data HARUS terurut!
data = [10, 25, 40, 50, 65, 77, 80, 93, 105, 120]
target_ditemukan = 77
target_tidak_ditemukan = 35

print("="*40)
print(f"Data List (Terurut): {data}")
print("="*40)

# --- Demo Binary Search ---
print("### HASIL PENCARIAN BINER (Binary Search) ###")

# Kasus ditemukan
idx_biner_found = binary_search(data, target_ditemukan)
if idx_biner_found != -1:
    print(f"Nilai {target_ditemukan} ditemukan pada indeks: {idx_biner_found}")
else:
    print(f"Nilai {target_ditemukan} tidak ditemukan.")

# Kasus tidak ditemukan
idx_biner_not_found = binary_search(data, target_tidak_ditemukan)
if idx_biner_not_found != -1:
    print(f"Nilai {target_tidak_ditemukan} ditemukan pada indeks: {idx_biner_not_found}")
else:
    print(f"Nilai {target_tidak_ditemukan} tidak ditemukan.")

print("="*40)

# --- Demo Interpolation Search ---
print("### HASIL PENCARIAN INTERPOLASI (Interpolation Search) ###")

# Kasus ditemukan
idx_inter_found = interpolation_search(data, target_ditemukan)
if idx_inter_found != -1:
    print(f"Nilai {target_ditemukan} ditemukan pada indeks: {idx_inter_found}")
else:
    print(f"Nilai {target_ditemukan} tidak ditemukan.")

# Kasus tidak ditemukan
idx_inter_not_found = interpolation_search(data, target_tidak_ditemukan)
if idx_inter_not_found != -1:
    print(f"Nilai {target_tidak_ditemukan} ditemukan pada indeks: {idx_inter_not_found}")
else:
    print(f"Nilai {target_tidak_ditemukan} tidak ditemukan.")
    
print("="*40)
