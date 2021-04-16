# masukkan jumlah nilai
n = int(input("Banyak nilai yang ingin dimasukkan: "))
data = []
print()

# pengulangan memasukkan nilai
i = 1
while i <= n:
    nilai = float(input("Masukkan nilai ke-%d: " %i))
    data.append(nilai)
    i = i + 1
print()
print("Data nilai: ", data)
print()

# menghitung nilai terkecil
import math
print("Nilai terkecil adalah ", min(data))
print()

# menghitung nilai terbesar
import math
print("Nilai terbesar adalah ", max(data))
print()

# menghitung nilai rata-rata
import math
rata_rata = sum(data) / n
print("Nilai rata-rata adalah ", rata_rata)
print()
