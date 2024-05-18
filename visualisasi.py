import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
# data = pd.read_csv("18.05.2024_06.39.30.784Z_Log.csv")
data = pd.read_csv("data_diperbaiki.csv")


# Menampilkan beberapa baris pertama dari data
print(data.head())

# Mengkonversi kolom 'time' menjadi datetime
# data["time"] = pd.to_datetime(data["time"])

# Menyiapkan plot
plt.figure(figsize=(12, 6))

# Membuat line plot untuk "Graph 0" dan "Graph 1"
# plt.plot(data.index, data["Graph 0"], label="Graph 0")
plt.plot(data.index, data["Graph 1"], label="Graph 1")

# Menambahkan judul dan label sumbu
plt.title("Visualisasi Data Graph 0 dan Graph 1")
plt.xlabel("nilai ke-")
plt.ylabel("Value")

# Menampilkan legenda
plt.legend()

# Menampilkan grid
plt.grid(True)

# Menampilkan plot
plt.show()
