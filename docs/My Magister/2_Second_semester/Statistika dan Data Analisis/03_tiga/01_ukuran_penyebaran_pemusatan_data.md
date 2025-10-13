# Ukuran penyebaran dan pemusatan data

Bogor, 30 September 2025 (Rumah baru, cerita baru, dan keberkahaan baru...)

!!! abstract "Sumber"

    - Pengantar Statistika dan Analisis Data PPT, Universitas Pamulang, DR. Tukiyat, M.SI.
    - Statistik Deksriptif for IT, Sudaryono, Asep Saefullah, dan Untung Rahardja

??? info "pretest"

    There is no pretest

## Definisi ukuran pemusatan

Dalam beberapa hal, ahli statisktik mengaggap rata-rata merupakan nilai yang cukup representatif bagi penggambaran nilai-nilai yang terdapat dalam data yang bersangkutan. Penilaian terhadap rata-rata berhubungan erat dengan dispersi atau variasi datanya dari mana rata-rata tersebut itu dihitung.

Ukuran kencendrungan memusat merupa suatu bilangan yang menunjukan tendensi (kencdrungan) memusatnya bilangan-bilangan dalam suatu distribusi.Ukuran tersebut dapat digunakan untuk merangkum data dan mendeskripsikan suatu kelompok variabel dengan cara mencari suatu angka (indeks) yang dapat mewakili seluruh kelompok tersebut. Rata-rata (Average) nilai yang mewakili himpunan. Nilai rata-rata cendrung terletak di tengah suatu kelompok data yang disusun menurut besar kecilnya nilai. Dengan kata lain ia mempunyai kencendrungan memusat

### Mean

Untuk menghitung nilai rata-rata dari himpunan dalam bentul table frekuensi kita harus;

1. Mencari nilai tengah dari setiap kelas $X$.
2. menghitung frekuensi dari setiap kelas $f$
3. $f \times x$

Ketika sudah dapat informasi diatas kita dapat menghitung rata-rata nilai dari himpunan table frekuensi dengan cara membagi jumlah perkalian nilia tengah dari setiap kelas dan frekuensi dengan banyak frekuensi nilai.

$$
\overline{X}=\frac{\sum{fx}}{N}
$$

_Case_

|Interval Nilai| $f$ (Frekuensi) |
| :--: | :--: |
| 33 - 39 | 2 |
| 26 - 32 | 8 |
| 19 - 25 | 19 |
| 12-18 | 20 |
| 5 - 11 | 11 |


??? question "Jawaban"

    Rata-rata nilai dari himpunan distirbusi frekuensi datas adalah **18.5**

    Jawaban dapat dilihat di [sini](./assets/1_average_distribusi_frekuensi.ipynb)


### Median
Jika ada himpunan data yang diurutkan dari bilangan terkecil hingga terbesar lalu dibagi menjadi dua kelompok; separuh masuk kedalam kelompok rendah dan sebagian masuk kedalam kelompok tinggi. Makak titik tengah yang memisahkan kedua kelompok tersebut disebut dengan _median_. Untuk memngetahui nilai tengah bergantung pada banyaknya data `n`, apakah ganjil atau genap.

!!! info "contoh"

    > Data Ganjil

    1,4,6,8,9, maka nilai tengahanya dapat kita ketetahui dengan $\frac{n}{2} + 0.5$. Contoh ini kita dapat index ke-3, maka nilai tengahanya adalah `6`. 

    > Data Genap

    1,4,6,8,9,10 maka nilai tengahanya dapat kita ketetahui dengan $\frac{n}{2} + 0.5$.  Contoh ini kita dapat index 3.5, , sehingga kita perlu mendapatkan nilai tengah antara index 3 dan index 4, sehingga nilai tengah adalah $\frac{4+8}{2}$, yaitu `7`.

Untuk menghitung median dari data frekuensi berkelompok kita dapat menggunakan persammaan dibawah ini


$$
{Median = B_{b} + (\frac{\frac{N}{2} - fk_{b}}{f_{d}}) \times i}
$$


$B_{b}$ = Batas bawah nyata dari interval yang mengandung median
$Fk_{b}$ = Frekuensi kumulatif dibawah interval yang mengandung median
$f_{d}$ = Frekuensi inteval yang mengandung nilai median
$i$ = Lebar interval
$N$ = Jumlah frekuensi dalam distribusi

_Case_

|Interval Nilai| $f$ (Frekuensi) |
| :--: | :--: |
| 33 - 39 | 2 |
| 26 - 32 | 8 |
| 19 - 25 | 19 |
| 12-18 | 20 |
| 5 - 11 | 11 |

Hitunglah nilai media dari data diatas

??? question "Jawaban"

    Nilai media dari himpunan distribusi frekuensi diatas adalah **16.67**

    Jawaban dapat dilihat di [sini](./assets/2_median_data_kelompok.ipynb)