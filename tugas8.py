# import library
from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

# inisialisasi fungsi
def tentukan(i):
   if i % 2 == 0:
      print(i+1, "Genap - ID proses", getpid())
   else:
      print(i+1, "Ganjil - ID proses", getpid())
   sleep(1)

# input
batas = int(input("Input:\n"))

print("\nOutput:")

# sekuensial
print("\nSekuensial")
sekuensial_awal = time()

for i in range(batas):
   tentukan(i)

sekuensial_akhir = time()

# multiprocessing.Process
print("\nmultiprocessing.Process")
kumpulan_proses = []

process_awal = time()

for i in range(batas):
   p = Process(target=tentukan, args=(i,))
   kumpulan_proses.append(p)
   p.start()

for i in kumpulan_proses:
   p.join()

process_akhir = time()

# multiprocessing.Pool
print("\nmultiprocessing.Pool")
pool_awal = time()

pool = Pool()
pool.map(tentukan, range(batas))
pool.close

pool_akhir = time()

# perbandingan waktu
print("\nWaktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process :", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool :", pool_akhir - pool_awal, "detik")

