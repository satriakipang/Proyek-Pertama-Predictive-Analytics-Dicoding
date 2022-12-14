# -*- coding: utf-8 -*-
"""Proyek Pertama Predictive Analytics Dicoding

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FDqFVC2n6j7ad1RU0U8EQ9kwsaaVKk-v

# 1. Instal dan import library
"""

#Instal requirement yang di butuhkan 
!pip install wget
!pip install opendatasets

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import sklearn
import opendatasets
import wget
import zipfile
from tqdm import tqdm
import os

os.environ['Your Kaggle username:'] = "fransiskusricardo"
os.environ['Your Kaggle Key:'] = "e178a4405fe43a23694788cd680b92fe"

"""#2. Load Dataset"""

if os.path.exists('diabetes-dataset/diabetes.csv'):
  print("file sudah ada")
else:
  opendatasets.download_kaggle_dataset(dataset_url='https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset', data_dir='')

data = pd.read_csv("diabetes-dataset/diabetes.csv")
data

data.shape

"""#3. Data understanding

Informasi data:

Attribute  | Keterangan
------------- | -------------
Sumber | https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset
Pregnancies | merepresentasikan Jumlah kehamilan
Glucose | merepresentasikan  tingkat Glukosa dalam darah
BloodPressure | merepresentasikan pengukuran tekanan darah 
SkinThickness | merepresentasikan ketebalan kulit
Insulin | merepresentasikan tingkat Insulin dalam darah       
BMI | merepresentasikan indeks massa tubuh
DiabetesPedigreeFunction  | merepresentasikan persentase diabetes
Age |merepresentasikan umur
Outcome |merepresentasikan hasil akhir 1 adalah diabetes dan 0 adalah Tidak diabetes

## 3.1. Mengecek tipe variabel pada data
"""

data.info()

"""## 3.2. Melihat jumlah data"""

print("Jumlah baris          :", data.shape[0])
print("Jumlah kolom          :", data.shape[1])

"""Data diabetes terdiri dari 768 baris, dan 9 kolom

## 3.3. Mengecek missing values
"""

pd.DataFrame({
    'missing value':data.isnull().sum()
})

"""Data diabetes tidak memiliki missing values untuk setiap kolomnya

###3.4. Mengecek double duplicated data
"""

data[data.duplicated()]

"""Hasil yang di peroleh adalah tidak ada data yang duplicated

## 3.5. Deskripsi statstik data
"""

data.describe()

"""Fungsi describe() memberikan informasi statistik pada masing-masing kolom, antara lain:

- **Count**  adalah jumlah sampel pada data.
- **Mean** adalah nilai rata-rata.
- **Std** adalah standar deviasi.
- **Min** yaitu nilai minimum setiap kolom. 
- **25%** adalah kuartil pertama. Kuartil adalah nilai yang menandai batas interval dalam empat bagian sebaran yang sama. 
- **50%** adalah kuartil kedua, atau biasa juga disebut median (nilai tengah).
- **75%** adalah kuartil ketiga.
- **Max** adalah nilai maksimum.

---
**Interpertasi Deskripsi statstik data**


Pada Kolom Glucose,	BloodPressure,	SkinThickness,	Insulin,	dan BMI memiliki nilai minimum yaitu 0. Hal tersebut tidak mungkin, sebab manusia tidak dapat mencapai nol untuk kadar glukosa, tekanan darah, ketebalan kulit, kadar insulin, dan BMI. Maka nilai nol pada kolom tersebut akan dihapus
"""

data = data.loc[(data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']]!=0).all(axis=1)]

data.describe()

data.shape

"""##3.6. Visualisasi data

###3.6.1. Kolom Pregnancies, dan  Outcome
"""

data_cols = ['Pregnancies', 'Outcome']
plt.figure(figsize = (15,8))
for i in range(len(data_cols)):
  plt.subplot(len(data_cols), 1, i + 1)  # i Rows , 1 cols 
  sns.boxplot(x = data[data_cols[i]])
  plt.title('Boxplot of {}'.format(data_cols[i]))
  plt.tight_layout()

"""###3.6.2. Kolom Glucose, BloodPressure, dan SkinThickness"""

data_cols = ['Glucose',	'BloodPressure', 'SkinThickness']
plt.figure(figsize = (15,12))
for i in range(len(data_cols)):
  plt.subplot(3, 1, i + 1)  # 3 Rows , 1 cols 
  sns.boxplot(x = data[data_cols[i]])
  plt.title('Boxplot of {}'.format(data_cols[i]))
  plt.tight_layout()

"""### 3.6.3. Kolom Insulin, BMI, DiabetesPedigreeFunction, Age"""

data_cols = ['Insulin',	'BMI', 'DiabetesPedigreeFunction',	'Age']
plt.figure(figsize = (15,12))

for i in range(len(data_cols)):
  plt.subplot(5, 1, i + 1)  # 3 Rows , 1 cols 
  sns.boxplot(x = data[data_cols[i]])
  plt.title('Boxplot of {}'.format(data_cols[i]))
  plt.tight_layout()

"""###3.6.4. Interpretasi Outlier pada Boxplot.

- Pada boxplot Pregnancies, plot menunjukkan outlier untuk jumlah kehamilan 13,15, 16, dan 17, data tersebut tidak dihapus karena seorang wanita mungkin melahirkan 17 anak.
- Pada boxplot Insulin, kadar insulin cukup berfluktuasi. Maka, tidak akan dianggap sebagai outlier
- Pada boxplot DiabetesPedigreeFunction, nilainya bervariasi berdasarkan riwayat keluarga. Maka, tidak akan menghapusnya.
- Pada boxplot Age, nilai umur terdapat outlier tetapi orang dengan usia seperti itu bisa ada. Maka, tidak akan dihapus.

##3.6. Menghapus outlier

Pada interpertasi Outlier pada Boxplot didapatkan data tidak dihapus, maka langkah ini di lewati

Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR=Q3-Q1
data=data[~((data<(Q1-1.5*IQR))|(data>(Q3+1.5*IQR))).any(axis=1)]
"""

data

"""#4. Univariate Analysis

Pertama, akan dibagi fitur pada dataset menjadi dua bagian, yaitu numerical features dan categorical features.
"""

numerical_features = ['Glucose',	'BloodPressure',	'SkinThickness',	'Insulin',	'BMI',	'DiabetesPedigreeFunction',	'Age']
categorical_features = ['Pregnancies','Outcome']

"""##4.1. Categorical Features

###4.1.1 Fitur Pregnancies
"""

feature = categorical_features[0]
count = data[feature].value_counts()
percent = 100*data[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""Melihat hasil data dan tidak ada korelasinya maka kolom data ini di hapus """

data.drop('Pregnancies', axis=1, inplace=True)

"""###4.1.2 Fitur Outcome"""

feature = categorical_features[1]
count = data[feature].value_counts()
percent = 100*data[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""##4.2. Numerical Features"""

plt.figure(figsize = (20,18))

for i in range(len(numerical_features)):
    plt.subplot(len(numerical_features), 1, i + 1)  # 2 Rows , 2 cols 
    sns.histplot(x = data[numerical_features[i]])
    plt.title('Displot of {}'.format(numerical_features[i]))
    plt.tight_layout()

"""Interpretasi histogram
- Beberapa kolom berdistribusi miring ke kanan
- Distribusi kolom yang berdistribusi normal adalah Glucose, BloodPressure, SkinThickness dan BMI.
- Distribusi harga miring ke kanan (right-skewed). adalah Insulin, DiabetesPedigreeFunction dan Age.

#5. Multivariate Analysis
"""

data

data.shape

"""## 5.1. Melihat Hubungan Antara Numerical Features Dengan Fungsi Tujuan Yaitu Outcome"""

for i in range(len(numerical_features)):
    plt.figure(figsize = (25,50))
    plt.subplot(len(numerical_features), 1, i + 1) 
    sns.kdeplot(x=data[numerical_features[i]], hue='Outcome',data=data)
    plt.title('Membandingkan distribusi {} penderita diabetes dan tanpa diabetes '.format(numerical_features[i]))
    plt.show()
    print('\n')

"""---------------------------
**Interpertasi**

Pada grafik perbandingan terdapat perbedaan yang terkena diabetes dan tidak diabetes, yaitu pada Glucose, BloodPressure, BMI, DiabetesPedigreeFunction, Age.

--------
**Kesimpulan**

Pada data tersebut kita bisa melihat bahwa ciri ciri pasien yang menderita diabetes memiliki kriteria yaitu :
- Pasien yang memiliki glucose tinggi
- Pasien yang memiliki BloodPressure tinggi
- Pasien yang memiliki BMI tinggi
- Pasein yang memiliki DiabetesPedigreeFunction tinggi
- Pasien yang memiliki Age lebih tua

##5.2 Heat Map
"""

plt.figure(figsize=(10, 8))
correlation_matrix = data.corr().round(2)
 
# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

"""-----
**Interpertasi**

Pada hasil heat map dapat dilihat bahwa diabetes berkorelasi dengan glucose, bmi dan age.

#6. Data Preparation

Balancing Dataset
"""

data_majority_0 = data[(data['Outcome']==0)] 
data_minority_1 = data[(data['Outcome']==1)] 


data_minority_upsampled = sklearn.utils.resample(data_minority_1, 
                                 replace=True,    
                                 n_samples= 260, 
                                 random_state=42) 

data = pd.concat([data_minority_upsampled, data_majority_0])

sns.countplot(x=data['Outcome'])

from sklearn.model_selection import train_test_split

X= data.drop(columns="Outcome")
y = data["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, shuffle=True, random_state=100)

"""# 7. Model Development

##7.1. K-Nearest Neighbor
"""

from sklearn.neighbors import KNeighborsClassifier
 
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train, y_train)

"""## 7.2. Random Forest"""

# Impor library yang dibutuhkan
from sklearn.ensemble import RandomForestClassifier

# buat model prediksi
RF = RandomForestClassifierModel = RandomForestClassifier(criterion = 'gini',n_estimators=100,max_depth=9,random_state=44) 
RF.fit(X_train, y_train)

"""##7.3. Boosting Algorithm"""

from sklearn.ensemble import AdaBoostClassifier
 
boosting = AdaBoostClassifier()                            
boosting.fit(X_train, y_train)

"""#8. Evaluasi Model"""

# Siapkan dataframe untuk analisis model
models = [knn, RF, boosting]
models_names= ["KNearestNeighbor","Random Forest","Boosting"]
mean_score = []

for model in models:
    cross_score = sklearn.model_selection.cross_val_score(model,X_train,y_train,cv=5)
    average_score = np.mean(cross_score)
    mean_score.append(average_score)

# Diagram Performances Models

plt.figure(figsize=(8,6))
sns.barplot(models_names,mean_score)
plt.title("Performance Models")
plt.show()

"""Pada diagram Permormance Models, Random Forest memiliki performance yang sangat baik. Maka kita akan gunakan Random Forest"""

print('Train RandomForestClassifierModel  : ' , RF.score(X_train, y_train))
print('Test RandomForestClassifierModel : ' , RF.score(X_test, y_test))

y_pred_RF = RandomForestClassifierModel.predict(X_test)
RF = sklearn.metrics.confusion_matrix(y_test,y_pred_RF)

ax=sns.heatmap(RF,annot=True,fmt=".2f")
ax.set_xticklabels(["Negatif", "Positif"])
ax.set_yticklabels(["Negatif", "Positif"])
plt.title("Confusion Matrix untuk Random Forest ")
plt.show()

RF_test_score = sklearn.metrics.accuracy_score(y_test,y_pred_RF)
print("Akurasi Random Forest Classifier : {}".format(RF_test_score))

print("-" * 100)

RF_precision_score = sklearn.metrics.precision_score(y_test,y_pred_RF)
print("Precision Random Forest Classifier : {}".format(RF_precision_score))

print("-" * 100)

RF_recall_score = sklearn.metrics.recall_score(y_test,y_pred_RF)
print("Recall Random Forest Classifier : {}".format(RF_recall_score))

print("-" * 100)

f1_score = sklearn.metrics.f1_score(y_test,y_pred_RF)
print("F1 score Random Forest Classifier : {}".format(f1_score))