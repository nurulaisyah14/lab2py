# input nilai integer
n = int(input("Masukkan nilai n: "))
t = int(input("Masukkan nilai t: "))

# Cetak nilai variabel
print("Variabel n:", n)
print("variabel t:", t)

# Cetak hasil operasi kedua variabel dengan string format
print("hasil penggabung {1} & {0}: %d".format (n, t) % (n + t))

# Konversi nilai variabel
n = int(n)
t =int(t)
print("Hasil penjumlahan {1} + {0}: %d".format(n, t) % (n + t))
print("Hasil pembagian {1} + {0}: %d".format(n, t) % (n / t))
