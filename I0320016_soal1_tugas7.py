# masukkan kalimat awal
print("Masukkan kalimat: ")
kalimat = str(input("<< "))
print()

# mengganti menjadi huruf kapital
print("Mengubah kalimat menjadi huruf kapital: ")
print(kalimat.upper())
print()

# menghitung jumlah huruf vokal
a = kalimat.count("a")
i = kalimat.count("i")
u = kalimat.count("u")
e = kalimat.count("e")
o = kalimat.count("o")
print("Jumlah huruf vokal dalam kalimat tersebut adalah ", a + i + u + e +o)
print()
