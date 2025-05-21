# Decission Trees


## Pretest

!!! question "Pertanyaan 1"
    Apa tujuan utama dari algoritma decision tree dalam klasifikasi?

    A. Untuk membagi data ke dalam kategori-kategori berdasarkan aturan yang mudah dipahami
    B. Untuk memprediksi nilai kontinu berdasarkan variabel input
    C. Untuk menganalisis data dalam bentuk grafik
    D. Untuk mengelompokkan data ke dalam beberapa kategori berdasarkan nilai numerik
    E. Untuk mengidentifikasi hubungan linier antara variabel

    ??? info "Jawaban"
        A. Untuk membagi data ke dalam kategori-kategori berdasarkan aturan yang mudah dipahami

!!! question "Pertanyaan 2"
    Bagaimana cara kerja algoritma decision tree?

    A. Dengan membuat grafik visualisasi untuk setiap data
    B. Dengan membuat prediksi berdasarkan rata-rata nilai data
    C. Dengan menggunakan probabilitas untuk setiap nilai dalam dataset 
    D. Dengan membagi data berdasarkan kriteria yang membagi dataset menjadi dua grup yang lebih homogen
    E. Dengan menghitung nilai kesalahan dan memperbaikinya di setiap iterasi

    ??? info "Jawaban"
        D. Dengan membagi data berdasarkan kriteria yang membagi dataset menjadi dua grup yang lebih homogen.

!!! question "Pertanyaan 3"
    Manakah yang bukan merupakan keuntungan dari penggunaan decision tree?

    A. Dapat menangani data yang bersifat numerik dan kategorikal
    B. Dapat menangani missing values dalam dataset
    C. Tidak memerlukan persiapan data atau pemrosesan sebelumnya
    D. Mudah untuk dipahami dan diinterpretasikan
    E. Mudah untuk digunakan dalam pemodelan regresi dan klasifikasi

    ??? info "Jawaban"
        C. Tidak memerlukan persiapan data atau pemrosesan sebelumnya

!!! question "Pertanyaan 4"
    Apa yang dimaksud dengan "overfitting" dalam konteks decision tree?

    A. Model gagal menghasilkan output yang valid
    B. Model tidak mampu mengklasifikasikan data dengan benar
    C. Model terlalu sederhana sehingga tidak dapat menangkap pola dalam data
    D. Model tidak menggunakan cukup fitur dalam proses pembuatan keputusan
    E. Model mempelajari detail yang sangat spesifik pada data pelatihan, sehingga kurang dapat generalisasi ke data baru

    ??? info "Jawaban"
        E. Model mempelajari detail yang sangat spesifik pada data pelatihan, sehingga kurang dapat generalisasi ke data baru

!!! question "Pertanyaan 5"
    Metrik evaluasi yang digunakan untuk mengukur kualitas model decision tree adalah:

    A. Koefisien determinasi (R²)
    B. Mean Squared Error (MSE)
    C. Akurasi dan F1-Score
    D. Akurasi dan Precision
    E. Koefisien regresi


    ??? info "Jawaban"
        C. Akurasi dan F1-Score

## Decission Tree

### Cost Complexity Prunning

CCP adalah sebuah teknik yang digunakan pada algoritma _Decission Tree_ untuk menghindari terjadinya overfitting dan meningkatkan peluang membuat model yang lebih umum. Teknin ini melibatkan 2 langkah;

1. Mengembangkan node tree hingga titik maksimal, tree dikembangkan terus hingga semua leave menjadi murni (Hanya ada satu pilahan pada setiap leave) atau hingga branch tidak bisa dikembangkan lagi sehingga tree memiliki banyak isntance.

2. Memangkasnya, selanjutnya memangkas kembali cabang-cabang yang tidak menghasilkan nilai prediksi yang signifika terhadap variabel tujuan. Prunning mempertimbangkan nilai ganti antara complexitas dari tree dan klasifikasi akurasi

[https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html#sphx-glr-auto-examples-tree-plot-cost-complexity-pruning-py](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html#sphx-glr-auto-examples-tree-plot-cost-complexity-pruning-py)


## Source

    * [Decission Tree Sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
    * [DT, good visualisation data even from looking for noise data](https://www.kaggle.com/code/hesankazemnia/mobile-price-classification-dt-rf-svm/notebook)
    * [Data diskrit dan kontinu](https://it.telkomuniversity.ac.id/data-diskrit-vs-data-kontinu/)
    * [Train Accuracy 100% and Test Accuracy less than that, it is posible as overfitting](https://stats.stackexchange.com/a/278931)
    * [More about overfitting](https://datascience.stackexchange.com/a/74686)