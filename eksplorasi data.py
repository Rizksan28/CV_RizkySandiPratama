import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset dari file Excel
file_path = "Dataset.xlsx"
df = pd.read_excel(file_path)

# Menampilkan informasi dataset
print(df.info())

# Menampilkan statistik deskriptif
print(df.describe())

# Menampilkan distribusi variabel numerik
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

# Plot histogram
plt.figure(figsize=(12, 8))
df[numerical_columns].hist(bins=30, figsize=(12, 10), layout=(4, 2), edgecolor='black')
plt.suptitle("Distribusi Variabel Numerik")
plt.show()

# Menampilkan boxplot untuk melihat outlier
plt.figure(figsize=(12, 8))
df[numerical_columns].boxplot(rot=45)
plt.title("Boxplot Variabel Numerik")
plt.show()

# Menampilkan korelasi antar variabel numerik
plt.figure(figsize=(10, 8))
corr_matrix = df[numerical_columns].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Heatmap Korelasi Antar Variabel Numerik")
plt.show()
