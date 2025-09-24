# Introduction to Statistics

Bogor, 08 September 2025 (Bogor dengan hawa gerahnya)

!!! abstract "Sumber"

    - Pengantar Statistika dan Analisis Data PPT, Universitas Pamulang, DR. Tukiyat, M.SI.
    - Introduction to Modern Statistics



??? info "pretest"

    **Satu**
    
    > Apa yang dimaksud dengan statistik deskriptif?


    * (A) Metode yang digunakan untuk menggambarkan dan meringkas data secara visual atau numerik.
    * (B) Cabang statistik yang digunakan untuk membuat inferensi tentang populasi berdasarkan sampel.
    * (C) Teknik yang digunakan untuk membuat inferensi atau kesimpulan dari data sampel ke populasi.
    * (D) Teknik yang digunakan untuk menguji hipotesis statistik.
    * (E) Metode untuk menentukan hubungan sebab-akibat antara variabel.

    ??? question "Jawaban"

        > Metode yang digunakan untuk menggambarkan dan meringkas data secara visual atau numerik

        Karena statistik deskriptif hanya berfokus pada pengolahan, penyajian, dan peringkasan data dalam bentuk tabel, grafik, diagram, rata-rata, median, modus, varians, standar deviasi, dll. Statistik ini tidak membuat inferensi atau generalisasi ke populasi, hanya mendeskripsikan data yang ada.

    **Dua**

    > Berikut ini yang bukan merupakan ukuran pemusatan dalam statistik adalah

    * (A) Ganjil
    * (B) Mean
    * (C) Modus
    * (D) Varians
    * (E) Median

    !!! question "Jawaban"

        Mean, Median, dan Modus → termasuk ukuran pemusatan (measures of central tendency), yang menggambarkan titik tengah atau nilai yang mewakili data.

        Varians → termasuk ukuran penyebaran (measures of dispersion), yang menunjukkan seberapa jauh data tersebar dari rata-rata.


    **Tiga**

    Apa tujuan utama dari analisa regresi dalam statistik ?

    * (A) Menentukan apakah suatu variabel memiliki hubungan kausal dengan variabel lain
    * (B) Memprediksi nilai suatu variabel berdasarkan variabel lain
    * (C) Menyajikan data dalam bentuk grafik
    * (D) Mengelompokkan data ke dalam kategori tertentu
    * (E) Menguji hipotesis tentang perbedaan antara kelompok.

    ??? question "Jawaban"

        analisis regresi digunakan untuk, Mengetahui hubungan antara variabel independen (X) dan variabel dependen (Y) dab Membuat model prediksi nilai Y berdasarkan X.

    **Empat**

    > Dalam distribusi normal, sekitar berapa persen data berada dalam rentang ±1 standar deviasi dari mean?

    * (A) 68%
    * (B) 95%
    * (C) 50%
    * (D) 40%
    * (E) 99%

    ??? question "Jawaban"

        Dalam distribusi normal berlaku Empirical Rule (Aturan 68-95-99,7):

        * standar deviasi dari mean → sekitar 68% data
        * standar deviasi dari mean → sekitar 95% data
        * standar deviasi dari mean → sekitar 99,7% data

    **Lima**

    Apa yang dimaksud dengan data kuantitatif?

    * (A) Data yang berbentuk kategori atau label
    * (B) Data yang berasal dari wawancara dan observasi kualitatif
    * (C) Data yang hanya dapat dikategorikan tetapi tidak memiliki urutan
    * (D) Data yang berbentuk angka dan dapat dihitung atau diukur
    * (E) Data yang berbentuk narasi, teks, atau gambar.

    ??? question "Jawaban"

        Data kuantitatif → berupa angka, bisa diukur, dihitung, dan dianalisis dengan operasi matematika/statistik (contoh: tinggi badan, umur, pendapatan).
        
        Data kualitatif → berupa kategori, label, atau deskripsi (contoh: jenis kelamin, warna mata, pekerjaan).



## Pengantar Statistika dan Data Analisis

Pada catatan ini insyaAllah akan dibahas beberapa pokok bahasan;

1. Data
2. Terminologi statistik
3. Statistika vs Statistik
4. Pengolahan Data
5. Penyajian Data

### Data

`Data` adalah sekumpulan fakta, kejadian atau peristiwa yang terjadi didalam atau diluar organisasi dalam bentuk angka, huruf,simbol, ataupun kombinasinya.

### Tipe-tipe data

!!! info "Berdasarkan sumber pengumpulan"

    `Data primer`, data yang diperoleh atau dikumpulkan oleh orang yang melakukan penelitian atau yang bersangkutan yang memerlukannya.

    `Data Sekunder`, data yang diperolah dari sumber-sumber yang telah ada.

!!! info "Berdasarkan pengumpulan"

    `Data Observasi` data atau informasi yang dihasilkan dengan cara {==mengamati secara langsung subjek==} atau fenomena yang diteliti baik melalui partisipasi peneliti dalam kegiatan atau hanya sebagai pengamat luar.

    `Studi literatur` adalah data sekunder yang diambil dari berbagai pustaka, seperti jurnal ilmiah, makalah seminar, buku, dan karya ilmiah yang relevan dengan penelitian. 

    `Kuisoner` adalah data yang dihasilkan secara langsung dari subjek penelitian melalui daftar  pertanyaan yang telah disusun sesuai tujuan penelitian. 

    `Wawancara` adalah data yang dihasilan secara langsung dari subjek penelitian dengan memberikan pertanyaan yang relevan dengan penelitian dan secara langsung didapatkan dari hasil wawancara.

!!! info "Berdasarkan banyak data"

    `Sensus` data yang dikumpulkan dari setiap unit dalam suatu populasi, bukan hanya sebagian (sampel) yang bertujuan untuk mendapatkan hasil yang lengkap mengenai krakteristik populasi tersebut dalam waktu tertentu.

    `sample` data yang diharapkan menggambarkan karakteristik dari sebuah populasi.

!!! info "Skala Pengukuran"

    `Data Nominal` data yang diberikan kepada objek tapi tidak menggambarkan kedudukan objek tersebut, hanya sebagai label.

    `Data Ordinal` data yang disusun menurut besarannya.

    `Data interval` data yang kategorinya diberikan berdasarkan jarak tertentu.

    `Data rasio` data yang memliki sifat nominal, ordinal dan interval. Angka yang pada data ini menggambarkan ukuran sebenarnya.

!!! info "Berdasarkan sifat"

    `Data kualitatif` data yang tidak berbentuk bilangan, namun dalam pengelolaanya akan dirubah kedalam bentuk bilangan yang diberikan label.

    `Data kuantitatif` data yang berbentuk bilangan.

### Terminologi dasar

Statistik adalah cabang dari Matematika yang mengubah data kedalam informasi yang berguna bagi pengambil keputusan. Statistik secara garis besar terbagi menjadi 2 bagian;

!!! note "Statistik Deskriptif"

    bagian ilmu statistik yang mengdeskripsikan data kedalam bentuk informasi yang mudah dicerna, seperti menghitung median, modus, rata2, variand, dsb. Pada statistik ini kita juga akan serin menjumpai berbagai macam bagan dan diagram.

    ``` mermaid
    graph LR
        A[Statistik Deskriptif] --> B[Frekuensi Distribusi];
        A --> C[Pemusatan central tedency];
        A --> D[Penyebaran Dispertion];
        C --> E[Mean, Median, Mode];
        D --> F[Range, Variance, Standard Deviation];
    ```

!!! note "Statistik Inferensial"

    Ilmu statistik yang membuat sebuah kesimpulan pada populasi berdasarkan hasil penghitungan statistik pada sample.

    ![alt text](assets/image.png)


### Prosedure pengujian Hipotesa

``` mermaid
stateDiagram-v2
    
    classDef badBadEvent fill:#f00,color:white,font-weight:bold,stroke-width:2px

    s1 : Menentukan hipotesa awal
    note right of s1
        Hipotesan nol Ho dan Hipotesa Alternatif H1
    end note
    s2 : Menentukan taraf nyata
    note left of s2
        Probabilitas menolak Hipotesa
    end note
    s3 : Menentukan uji statistik
    note right of s3
        Alat uji statistik, uji Z, t, F, X2 dan lain-lain
    end note
    s4 : Menentukan daerah keputusan
    note left of s4
        Daerah dimana hipotesa nol diterima atau ditolak
    end note
    s5 : Mengambil keputusan
    sOke : Hipotesa diterima
    sTidak : Hipotesa ditolak
    [*] --> s1
    s1 --> s2
    s2 --> s3
    s3 --> s4
    s4 --> s5
    s5 --> sOke
    s5 --> sTidak:::badBadEvent
```


### Apa manfaat dari statistik

Menggunakan statistik kita dapat mengetahui hubungan antar variable, variabel independen dan vari dependend, dimana varial dependen dipengaruhi oleh variabel independen, sehingga kita dapat membuat peralaman secara kita mengetahui fungsi pengaruh variabel2 tersebut dan membuat keputusan atas peralaman.

## Data analisis
Data analisis adalah proses pengumupulan data, pemodelan, dan analisa data menggunakan berbagai metode statistik. praktik bekerja dengan data untuk mengumpulkan informasi yang berguna yang mana informasi tersebut dapat digunakan untuk pengambilan keputusan.

!!! info "Alur pengolahan data"

    ``` mermaid
    graph LR
        A[Mengunpulkan fakta] --> B[Peroses pengambilan data];
        B --> C[Proses analisis data];
        C --> D[Deksripsi hasil pengolahan data];
    ```

## 5 Tipe Analisis

!!! info "Analisa Deskriptif"

    Analisa yang memberikan deksripsi yang terjadi pada masa lalu atau mendeskrpisikan objek dengan narasi ssuai dengan data yang tersedia dan membantu bisnis untuk mengetahui kinerjanya dengan memberikan konteks untuk membantu pemangku kepentingan menafsirkan informasi.


!!! info "Analisa Diagnostik"

    Memprediksi apa yang paling mungkin terjadi dimasa depan dan memberikan pengetahuan/wawasan yang dapat ditindaklanjuti berdasarkan informasi tersebut.


!!! info "Analisa Predikif"

    Mengambil hasil analisa deksriptif, dan menganalisa lebih lanjut untuk mengetahui informasi mengapa sesuatu terjadi dimasa lalu.

!!! info "Analisa Preskriptif"

    Memberikan informasi mengenai tindakan yang akan memanfaatn prediksi dan membantu tindakan yang mungkin untuk memberikan solusi.

----

_Muhammad Farras Ma'ruf, di Parung, Bogor. 2025-09-24_