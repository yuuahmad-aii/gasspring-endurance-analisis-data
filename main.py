import pandas as pd
from datetime import datetime, timedelta

# Membaca data dari file CSV
data = pd.read_csv("data_mentah.csv")

# Menampilkan beberapa baris pertama dari data untuk verifikasi
print("Data asli:")
print(data.head())

# Membulatkan nilai di kolom "Graph 0"
# data["Graph 0"] = data["Graph 0"].apply(np.round)
data["Graph 0"] = data["Graph 0"].round().astype(int)
data["Graph 2"] = data["Graph 2"].round().astype(int)

# Menampilkan data setelah pembulatan untuk verifikasi
print("\nData setelah pembulatan:")
print(data.head())

# Mengelompokkan data berdasarkan nilai "Graph 1" dan menemukan nilai maksimum "Graph 2" untuk setiap kelompok
max_values = data.groupby("Graph 0")["Graph 1"].max().reset_index()

# Menampilkan hasil
print("\nNilai maksimum pada 'Graph 1' untuk setiap nilai unik di 'Graph 0':")
print(max_values)

# Menambahkan kolom datetime dengan jeda 5 detik dimulai dari 2023-12-06 08:05:59
start_time = datetime(2023, 12, 6, 8, 5, 59)
time_delta = timedelta(seconds=5)
datetime_list = [start_time + i * time_delta for i in range(len(max_values))]

# Menambahkan kolom tanggal dan waktu terpisah
max_values["date"] = [dt.date() for dt in datetime_list]
max_values["time"] = [dt.time() for dt in datetime_list]

# Menampilkan hasil setelah menambahkan kolom tanggal dan waktu
print("\nData dengan kolom tanggal dan waktu:")
print(max_values)

# Menyimpan hasil ke file CSV baru
max_values.to_csv("data_diperbaiki.csv", index=False)
