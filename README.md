# Laporan Proyek Machine Learning - Fransiskus Ricardo

## Domain Proyek

Perkembangan *Machine Learning* yang sangat pesar dapat membantu manusia dalam menyelesaikan permasalahan yang rumit dengan komputasi komputer. Pada proyek ini penulis ingin menggunakan *Machine Learning* untuk memprediksi diabetes pada pasien. 

Diabetes melitus (DM) didefinisikan sebagai suatu penyakit atau gangguan metabolisme kronis dengan multi etiologi yang ditandai dengan kadar gula darah di atas atau sama dengan 200 mg/dl, dan kadar gula darah puasa di atas atau sama dengan 126 mg/dl, disertai dengan gangguan metabolisme karbohidrat, lipid, dan protein sebagai akibat insufisiensi fungsi insulin. Insufisiensi fungsi insulin dapat disebabkan oleh gangguan atau defisiensi produksi insulin oleh sel-sel beta Langerhans kelenjar pankreas, atau disebabkan oleh kurang responsifnya sel-sel tubuh terhadap insulin [Kemenkes RI](https://p2ptm.kemkes.go.id/informasi-p2ptm/penyakit-diabetes-melitus). DM dikenal sebagai silent killer karena sering tidak disadari oleh penyandangnya dan saat diketahui sudah terjadi komplikasi (Kemenkes RI, 2014). DM dapat menyerang hampir seluruh sistem tubuh manusia, mulai dari kulit sampai jantung yang menimbulkan komplikasi. Penyakit Diabetes Mellitus merupakan ranking keenam penyebab kematian di Dunia, hal ini diungkapkan oleh dunia World Health Organization (WHO). 

Oleh karena DM merupakan penyakit yang sangat berbahaya. Penulis ingin memprediksikan penyakit DM pada pasien dengan 3 model yaitu KNN Classifier, Random Forest Classifier dan Boost Classifier pada dataset di [Kaggle](https://www.kaggle.com).


## Business Understanding
Berdasarkan latar belakang yang sudah dipaparkan sebelumnya, berikut rincian masalah yang dapat diselesaikan dalam proyek ini :
- Bagaimana cara membuat model machine learning untuk mengklasifikasikan pasien yang menderita diabetes dan tidak?
- Apa faktor yang membuat pasien menglami diabetes?

### Goals
Menjelaskan tujuan dari pernyataan masalah:
- Jawaban pernyataan masalah 1
- Jawaban pernyataan masalah 2
- Jawaban pernyataan masalah n

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Menambahkan bagian “Solution Statement” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 

    ### Solution statements
    - Mengajukan 2 atau lebih solution statement. Misalnya, menggunakan dua atau lebih algoritma untuk mencapai solusi yang diinginkan atau melakukan improvement pada baseline model dengan hyperparameter tuning.
    - Solusi yang diberikan harus dapat terukur dengan metrik evaluasi.

## Data Understanding
Paragraf awal bagian ini menjelaskan informasi mengenai data yang Anda gunakan dalam proyek. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- accepts : merupakan jenis pembayaran yang diterima pada restoran tertentu.
- cuisine : merupakan jenis masakan yang disajikan pada restoran.
- dst

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.


