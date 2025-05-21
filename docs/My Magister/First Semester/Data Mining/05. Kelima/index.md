1. Tujuan utama dari algoritma Naïve Bayes dalam klasifikasi:
✅ Jawaban: D. Mengklasifikasikan teks ke dalam kategori berdasarkan probabilitas
🔍 Penjelasan: Naïve Bayes digunakan untuk mengklasifikasikan teks (misalnya spam atau bukan spam) berdasarkan probabilitas kemunculan kata-kata dalam teks tersebut.
Algoritma Naïve Bayes adalah metode klasifikasi yang berbasis pada teori probabilitas Bayes dengan asumsi independensi antar fitur (karena itu disebut “naïve”). Tujuan utamanya adalah untuk mengklasifikasikan data (sering kali teks) ke dalam kategori tertentu berdasarkan probabilitas kemunculan fitur-fitur dalam data tersebut.

Misalnya, dalam klasifikasi email sebagai spam atau bukan spam, Naïve Bayes menghitung probabilitas bahwa sebuah email tergolong spam berdasarkan kata-kata yang muncul di dalamnya.

2. Prinsip dasar dari algoritma Naïve Bayes:
✅ Jawaban: A. Asumsi bahwa fitur dalam data bersifat independen satu sama lain
🔍 Penjelasan: Naïve Bayes mengasumsikan bahwa fitur (kata-kata) saling independen secara bersyarat, yang membuat perhitungannya sederhana dan cepat.

Penjelasan:
Prinsip dasar dari algoritma Naïve Bayes adalah asumsi independensi bersyarat antar fitur. Artinya, algoritma ini mengasumsikan bahwa keberadaan (atau nilai) suatu fitur tidak bergantung pada fitur lain, dengan syarat kelas tertentu sudah diketahui.

Contoh sederhananya: dalam klasifikasi email, jika ada dua kata seperti “gratis” dan “promo”, Naïve Bayes menganggap kemunculan kata “gratis” tidak terpengaruh oleh kemunculan kata “promo”, meskipun dalam kenyataannya mungkin saja keduanya sering muncul bersamaan di email spam. Ini yang disebut “naïve” (naif), karena menyederhanakan kenyataan.

Tapi justru karena kesederhanaan inilah, Naïve Bayes sering efektif dan sangat cepat, terutama dalam masalah klasifikasi teks.

3. Fitur yang sering digunakan dalam Naïve Bayes untuk klasifikasi teks:
✅ Jawaban: E. Kata-kata dalam teks
🔍 Penjelasan: Kata-kata (tokens) dalam teks digunakan sebagai fitur utama dalam model Naïve Bayes, biasanya melalui pendekatan Bag of Words.

Penjelasan:
Dalam klasifikasi teks menggunakan algoritma Naïve Bayes, fitur yang paling sering digunakan adalah kata-kata dalam teks (biasa disebut features atau tokens). Pendekatan umum yang digunakan adalah Bag of Words (BoW), di mana setiap kata dalam korpus dianggap sebagai fitur, dan setiap dokumen (misalnya email, artikel, tweet) direpresentasikan sebagai vektor jumlah atau keberadaan kata-kata tersebut.

Contoh: Kalau kamu punya kalimat "Saya suka kopi", maka kata "saya", "suka", dan "kopi" masing-masing menjadi fitur. Kemudian Naïve Bayes menghitung probabilitas sebuah dokumen termasuk ke dalam kategori tertentu (misalnya "positif" atau "negatif") berdasarkan frekuensi atau keberadaan kata-kata tersebut.

Kalau kamu mau, aku bisa tunjukin contoh kecil bagaimana teks diubah jadi fitur buat Naïve Bayes. Mau?

4. Keuntungan dari menggunakan Naïve Bayes dalam klasifikasi teks:
✅ Jawaban: B. Dapat menangani teks yang sangat besar dengan cepat
🔍 Penjelasan: Naïve Bayes bekerja efisien dan cepat, bahkan pada dataset besar dan berdimensi tinggi seperti teks.

Penjelasan:
Salah satu keuntungan utama Naïve Bayes dalam klasifikasi teks adalah:

Cepat dan efisien, bahkan saat digunakan pada dataset yang besar dan berdimensi tinggi, seperti dokumen teks dengan ribuan kata unik.

Mudah diimplementasikan dan tidak membutuhkan sumber daya komputasi besar, cocok untuk aplikasi real-time seperti filtering email spam, analisis sentimen, dll.

Mari bahas pilihan lain dengan cepat:

A. Salah – Naïve Bayes bisa digunakan untuk data non-numerik, seperti teks.

C. Salah – Justru Naïve Bayes bisa bekerja baik meskipun dengan data pelatihan yang relatif sedikit.

D. Salah – Naïve Bayes itu termasuk algoritma yang sederhana dan mudah dipahami.

E. Salah – Naïve Bayes bekerja baik pada data berdimensi tinggi, seperti teks (di mana setiap kata bisa jadi fitur).

5. Tahap penerapan Naïve Bayes terhadap dataset teks:
✅ Jawaban: B. Setiap kata atau token diubah menjadi fitur yang dapat dihitung probabilitasnya
🔍 Penjelasan: Teks diubah menjadi fitur (kata-kata) yang dapat digunakan untuk menghitung probabilitas kelas pada model klasifikasi.

Penjelasan:
Dalam penerapan Naïve Bayes untuk klasifikasi teks, langkah pentingnya adalah mengubah teks menjadi representasi fitur. Biasanya, ini dilakukan dengan:

Tokenisasi – memecah teks menjadi kata-kata (tokens).

Representasi fitur – setiap kata dianggap sebagai fitur.

Menghitung frekuensi atau keberadaan kata dalam dokumen.

Menghitung probabilitas setiap kata muncul dalam kelas tertentu berdasarkan data pelatihan.

Misalnya, jika kamu punya dokumen:

"Kopi enak dan hangat"

Maka fitur bisa berupa: {kopi, enak, dan, hangat}
Naïve Bayes akan menghitung probabilitas dokumen termasuk dalam suatu kelas (misalnya “positif” atau “netral”) berdasarkan kata-kata tersebut.

Jadi bukan asal-asalan hitung, tapi pakai pendekatan probabilistik yang cerdas

## Naive Bayes

Sebelum kita mempelajarin `Multinomial Naive Bayes` kita harus memahami dahulu apa itu `Naive Bayes`. Untuk pengetahuan, ada versi dari `Naive Bayes` yang juga biasa digunakan, yaitu `Gaussian Naive Bayes Classification`.

[Source Stat quest](https://www.youtube.com/watch?v=O2L2Uv9pdDA&t=886s)

