
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


data = pd.read_csv('nilai_siswa.csv', sep=';') 


data.info() 

data.head() 

data.describe()

print("Rata-rata:", data['Nilai'].mean()) 
print("Median:", data['Nilai'].median()) 
print("Modus:", data['Nilai'].mode()[0]) 


matematika = data[data['Mapel'] == 'Matematika'] 
print("\n--- Nilai Matematika ---")
print(matematika)

bahasa_inggris = data[data['Mapel'] == 'Bahasa Inggris']
print("\n--- Nilai Bahasa Inggris ---")
print(bahasa_inggris)

bahasa_indonesia = data[data['Mapel'] == 'Bahasa Indonesia']
print("\n--- Nilai Bahasa Indonesia ---")
print(bahasa_indonesia)

produktif = data[data['Mapel'] == 'Produktif']
print("\n--- Nilai Produktif ---")
print(produktif)

print("\n--- Nilai Maksimum dan Minimum per Mata Pelajaran ---")
print(data.groupby('Mapel')['Nilai'].agg(['max', 'min']))

rata_rata_mapel = data.groupby('Mapel')['Nilai'].mean()
rata_rata_mapel.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sns.boxplot(x='Mapel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()

# Jawaban No 1 = Fisika
# Jawaban No 2 = Bahasa Indonesia
# Jawaban No 3 = Dengan Visualisasi kita lebih mudah memahami data karena disajikan dalam bentuk grafik yang menarik dan informatif.

# Refleksi: 
#  Jawaban No 1 = Cara membuat visualisasi data, dengan menggunakan visualisasi data, kita dapat dengan mudah mengidentifikasi pola, tren, dan outlier dalam data nilai.
#  Jawaban No 2 = Kesulitan dalam bagaimana memahami cara kerja fungsi dalam membuat grafik
#  Jawaban No 3 = Ai yang paling membantu dalam analysis data adalah ChatGPT, dan QWEEN, karena memberikan analysis data yang hampir lengkap dan mudah di pahami.