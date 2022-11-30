# Laporan Proyek Machine Learning - Fransiskus Ricardo

## Domain Proyek

Perkembangan *Machine Learning* yang sangat pesat dapat membantu manusia dalam menyelesaikan permasalahan yang rumit dengan komputasi komputer. Pada proyek ini penulis ingin menggunakan *Machine Learning* untuk memprediksi diabetes pada pasien. 

Diabetes melitus (DM) didefinisikan sebagai suatu penyakit atau gangguan metabolisme kronis dengan multi etiologi yang ditandai dengan kadar gula darah di atas atau sama dengan 200 mg/dl, dan kadar gula darah puasa di atas atau sama dengan 126 mg/dl, disertai dengan gangguan metabolisme karbohidrat, lipid, dan protein sebagai akibat insufisiensi fungsi insulin. Insufisiensi fungsi insulin dapat disebabkan oleh gangguan atau defisiensi produksi insulin oleh sel-sel beta Langerhans kelenjar pankreas, atau disebabkan oleh kurang responsifnya sel-sel tubuh terhadap insulin [Kemenkes RI](https://p2ptm.kemkes.go.id/informasi-p2ptm/penyakit-diabetes-melitus). DM dikenal sebagai silent killer karena sering tidak disadari oleh penyandangnya dan saat diketahui sudah terjadi komplikasi (Kemenkes RI, 2014). DM dapat menyerang hampir seluruh sistem tubuh manusia, mulai dari kulit sampai jantung yang menimbulkan komplikasi. Penyakit Diabetes Mellitus merupakan ranking keenam penyebab kematian di Dunia, hal ini diungkapkan oleh dunia World Health Organization (WHO). 

Oleh karena DM merupakan penyakit yang sangat berbahaya. Penulis ingin memprediksikan penyakit DM pada pasien dengan 3 model yaitu KNN Classifier, Random Forest Classifier dan Boost Classifier pada dataset di [Kaggle](https://www.kaggle.com).


## Business Understanding
Berdasarkan latar belakang yang sudah dipaparkan sebelumnya, berikut rincian masalah yang dapat diselesaikan dalam proyek ini :
- Bagaimana cara membuat model machine learning untuk mengklasifikasikan pasien yang menderita diabetes dan tidak?
- Apa faktor yang membuat pasien mengalami diabetes?


### Goals
- Mengetahui model yang mempunyai akurasi tinggi untuk prediksi diabetes pada pasien.

    ### Solution statements
    - Melakukan proses *Exploratory Data Analysis* untuk melihat data yang memiliki pengaruh terbesar kepada pasien yang terkena diabetes.
    - Menggunakan model *Machine Learning* untuk memprediksi pasien yang terkena diabetes. Berikut model-model yang akan digunakan:
    - *Random Forest Classifier*
    - *K-Neighbors Classifier*
    - *AdaBoost Classifier*

## Data Understanding
Dataset yang digunakan untuk memprediksi pasien diabete yang diambil dari platform kaggle.com yang dipublikasikan oleh AKSHAY DATTATRAY KHARE. Dataset Dataset ini berasal dari National Institute of Diabetes and Digestive and Kidney Diseases. 
Tujuan dari dataset ini adalah untuk memprediksi secara diagnostik apakah seorang pasien menderita diabetes, berdasarkan pengukuran diagnostik tertentu yang termasuk dalam kumpulan data. Dataset ini terdiri dari 1 file csv. 

### Informasi data:

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

Pada berkas berisikan informasi pasien sebanyak 768 data dengan 9 kolom serta terdapat 0 missing values dan 0 duplicated data.

### Berikut rangkuman `statistik deskriptif` dari fitur dalam dataset: <br>
<img src="image/statistik_deskriptif_numeric.png" style="zoom:150%;" /><br>

#### Interpretasi Deskripsi statistik data
Pada Kolom Glucose, BloodPressure, SkinThickness, Insulin, dan BMI memiliki nilai minimum yaitu 0. Hal tersebut tidak mungkin, sebab manusia tidak dapat mencapai nol untuk kadar glukosa, tekanan darah, ketebalan kulit, kadar insulin, dan BMI. Maka nilai nol pada kolom tersebut akan dihapus. <br>
<img src="image/statistik_deskriptif_numeric_revisi.png" style="zoom:150%;" /><br>


### Berikut Visualisasi data dengan Boxplot: <br>
<img src="image/Visualisasi _boxplot1.png" style="zoom:70%;" /> <br>
<img src="image/Visualisasi _boxplot2.png" style="zoom:70%;" /> <br>
<img src="image/Visualisasi _boxplot3.png" style="zoom:70%;" /> <br>

#### Interpretasi Outlier pada Boxplot.
- Pada boxplot Pregnancies, plot menunjukkan outlier untuk jumlah kehamilan 13,15, 16, dan 17, data tersebut tidak dihapus karena seorang wanita mungkin melahirkan 17 anak.
- Pada boxplot Insulin, kadar insulin cukup berfluktuasi. Maka, tidak akan dianggap sebagai outlier
- Pada boxplot DiabetesPedigreeFunction, nilainya bervariasi berdasarkan riwayat keluarga. Maka, tidak akan menghapusnya.
- Pada boxplot Age, nilai umur terdapat outlier tetapi orang dengan usia seperti itu bisa ada. Maka, tidak akan dihapus. <br>


### Berikut Visualisasi data Categorical Features pada plot : <br>
<img src="image/Visualisasi _Categorical_Features1.png" style="zoom:70%;" /> 
<img src="image/Visualisasi _Categorical_Features2.png" style="zoom:70%;" /><br>

#### Interpretasi plot
- Melihat hasil data Pregnancies dan tidak ada korelasinya maka kolom data Pregnancies di hapus. <br>


### Berikut Visualisasi data Numerical Features pada histogram :
<img src="image/Visualisasi _Numerical_Features1.png" style="zoom:70%;" /><br> 
<img src="image/Visualisasi _Numerical_Features2.png" style="zoom:70%;" /><br>

#### Interpretasi histogram
- Beberapa kolom berdistribusi miring ke kanan
- Distribusi kolom yang berdistribusi normal adalah Glucose, BloodPressure, SkinThickness dan BMI.
- Distribusi harga miring ke kanan (right-skewed). adalah Insulin, DiabetesPedigreeFunction dan Age.<br>


### Multivariate Analysis
Melihat Hubungan Antara Numerical Features Dengan Fungsi Tujuan Yaitu Outcome.
<img src="image/Multivariate_Analysis1.png" style="zoom:70%;" /><br>
<img src="image/Multivariate_Analysis2.png" style="zoom:70%;" /><br>
<img src="image/Multivariate_Analysis3.png" style="zoom:70%;" /><br>
<img src="image/Multivariate_Analysis4.png" style="zoom:70%;" /><br>

#### Interpertasi
- Pada grafik perbandingan terdapat perbedaan yang terkena diabetes dan tidak diabetes, yaitu pada Glucose, BloodPressure, BMI, DiabetesPedigreeFunction, Age.<br>


### Heat Map
<img src="image/Heat_Map.png" style="zoom:70%;" /><br>

#### Interpertasi
- Pada hasil heat map dapat dilihat bahwa diabetes berkorelasi dengan glucose, bmi dan age.

### Kesimpulan
Pada data tersebut kita bisa melihat bahwa ciri ciri pasien yang menderita diabetes memiliki kriteria yaitu :
- Pasien yang memiliki glucose tinggi
- Pasien yang memiliki BloodPressure tinggi
- Pasien yang memiliki BMI tinggi
- Pasien yang memiliki DiabetesPedigreeFunction tinggi
- Pasien yang memiliki Age lebih tua

## Data Preparation

- Mengatasi *outlier*
  Pada tahapan ini berguna untuk menghapus data tidak normal pada dataset yang telah di buat pada boxplot.  


- Mengatasi data kosong <br>
  <img src="image\missing_value.png" style="zoom:70%;" /><br>
  Tahapan ini bertujuan untuk mengisi data yang tidak lengkap atau data kosong. 


- Mengatasi duplicated data <br>
 <img src="image\duplicated_data.png" style="zoom:70%;" /><br>
 Hasil yang di peroleh adalah tidak ada data yang duplicated


- Balancing Dataset <br>
 <img src="image\Balancing_Dataset.png" style="zoom:70%;" /><br>
  Pada tahapan Balancing Dataset diperlukan untuk menyeimbangan data Outcome yang tidak seimbang, jika tidak seimbangan maka model cenderung mengarah pada kategori yang lebih banyak datanya. Oleh sebab itu tahapan Balancing Dataset dilakukan, teknik ini membuat data dummy atau data buatan. 


- Membagi data menjadi data *training* dan *testing*
  Tahapan ini bertujuan agar model yang dilatih dapat diuji dengan data yang berbeda dari data yang digunakan dalam pelatihan. Data dapat dibagi menjadi dua bagian yaitu *training* dan *testing*. Pembagian datanya yaitu persentase untuk *training* sebesar 80% dan sisanya 20% untuk *testing*. Fungsi [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) pada library sklearn yang akan digunakan untuk menangani tahapan ini.



## Modeling
Algoritma pada *Machine Learning* yang digunakan antara lain : 
- **K-Neighbors Classifier**, K-Nearest Neighbour bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat. Pada penelitian ini merupakan masalah klasifikasi makan akan membandingkan 2 data. Proyek ini menggunakan [sklearn.neighbors.KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html?highlight=kneighborsclassifier#sklearn.neighbors.KNeighborsClassifier) dengan memasukkan X_train dan y_train dalam membangun model. Parameter yang digunakan pada proyek ini yaitu `n_neighbors` = Jumlah k tetangga terdekat.
    
- **Random Forest Classifier**, merupakan salah satu algoritma populer yang digunakan karena kesederhanaannya dan memiliki stabilitas yang baik. Proyek ini menggunakan [sklearn.ensemble.RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html?highlight=sklearn+ensemble+randomforestclassifier#sklearn.ensemble.RandomForestClassifier) dengan memasukkan X_train dan y_train dalam membangun model. Parameter yang digunakan pada proyek ini adalah :
     `criterion` = Fungsi untuk mengukur kualitas split..
     `n_estimators` = Jumlah tree pada forest.
     `max_depth` = Kedalaman maksimum setiap tree.
     `random_state` = Mengontrol seed acak yang diberikan pada setiap base_estimator pada setiap iterasi.

- **AdaBoost Classifier**, merupakan singkatan dari Adaptive Boosting Classifier. Algoritma ini bertujuan untuk memberikan bobot lebih pada observasi yang tidak tepat atau disebut weak classification. Proyek ini menggunakan [sklearn.ensemble.AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html?highlight=sklearn+ensemble+adaboostclassifier#sklearn.ensemble.AdaBoostClassifier) dengan memasukkan X_train dan y_train dalam membangun model. 



## Evaluation
Pada proyek ini model dibuat untuk mengklasifikasikan pasien terkena diabetes dan tidak terkena diabetes. Hasil evaluasi diperoleh bahwa model yang memiliki Performance tertinggi iyalah Random Forest Classifier. <br>
<img src="image\Performance_Models.png" style="zoom:70%;" /><br>

Sebelum menghitung Accuracy, Precision, Recall, dan F1-score. Akan dijelaskan mengenai *confusion matrix* terdapat empat nilai, yakni *true positive*,  *true negative*, *false positive* dan *false negative*. Untuk lebih jelasnya perhatikan gambar dibawah ini. <br>

<img src="image\cm1.jpg" style="zoom:50%;" /><br>

- *Accuracy*

  *Metrics* akurasi sebagai tingkat kedekatan antara nilai prediksi dengan nilai aktual, untuk menghitungnya hanya tinggal membagi jumlah benar dibagi keseluruhan data. akurasi  cocok digunakan dalam kasus data yang seimbang. 

- *Precision*

  *Metrics* ini mengukur tingkat ketepatan antara informasi yang diminta oleh pengguna dengan jawaban yang diberikan oleh sistem. Untuk menghitung nilai dari *precision* dapat dilihat pada formula di bawah ini. <br>

  <img src="image\precision.png" style="zoom:80%;" /><br>

  *Metriks* ini hanya berfokus pada performa  model dalam memprediksi terhadap label data positif. 

- *Recall*

  *Metrics* ini mengukur tingkat keberhasilan sistem dalam menemukan kembali sebuah informasi. Untuk menghitung nilai dari recall dapat dilihat pada formula di bawah ini. <br>

  <img src="image\recall.png" style="zoom:80%;" /><br>

  Tidak seperti precision yang hanya memperhitungkan label positif, metriks ini menghitung bagian negatif dari prediksi label positif. 

- *F1-score*

  *Metrics* ini merupakan rata-rata harmonik dari precission dan recall. Untuk menghitung nilai dari *f1-score* dapat dilihat pada formula di bawah ini.<br>

  <img src="image/f1_score.png" style="zoom: 40%;" /><br>

Selanjutnya model Random Forest Classifier, akan dihitung *metrics* f1-score dan recall. <br>
<img src="image\Confusion_Matrix_untuk_Random_Forest.png" style="zoom:70%;" /><br>
<img src="image\Nilai_Akurasi_Precision_Recall_F1.png" style="zoom:70%;" /><br>

## Kesimpulan
Kesimpulan dari proyek prediksi pasien diabetes dan tidak diabetes dengan menggunakan tiga model *Machine Learning*, yaitu bahwa diantara *K-Neighbors Regressor Classifier*, *Random Forest Classifier*, dan *AdaBoost Classifier*. Diperoleh bahwa algoritma *Random Forest Classifier* lebih baik dibandingkan yang lainnya. Hal ini dapat dilihat dari performance model yang tinggi dibandingkan algoritma yang lainnya. 

Pada data tersebut kita bisa melihat bahwa ciri ciri pasien yang menderita diabetes memiliki kriteria yaitu :
    - Pasien yang memiliki glucose tinggi
    - Pasien yang memiliki BloodPressure tinggi
    - Pasien yang memiliki BMI tinggi
    - Pasien yang memiliki DiabetesPedigreeFunction tinggi
    - Pasien yang memiliki Age lebih tua


# Referensi

1. [Dicoding](https://www.dicoding.com/academies/319/tutorials/16979?from=17053) (2021). *Machine learning Terapan*
2. [Scikit-learn](https://scikit-learn.org/). *Documentation*
3. [Imbalanced-learn](https://imbalanced-learn.org/stable/). *Documentation*
4. [Kemenkes RI](https://p2ptm.kemkes.go.id/informasi-p2ptm/penyakit-diabetes-melitus) 
