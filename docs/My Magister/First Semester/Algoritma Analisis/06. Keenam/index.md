## Pretest

1. Apa yang dimaksud dengan algoritma Greedy?

A.

B) Algoritma yang selalu memilih langkah terbaik saat ini tanpa mempertimbangkan konsekuensi di masa depan

B.

C) Algoritma yang mengutamakan efisiensi ruang dibandingkan waktu

C.

A) Algoritma yang mencoba semua kemungkinan solusi secara brute force

D.

E) Algoritma yang selalu menghasilkan solusi optimal

E.

D) Algoritma yang hanya bekerja pada struktur data berbasis pohon



ChatGPT said:
Jawaban yang benar adalah:

B) Algoritma yang selalu memilih langkah terbaik saat ini tanpa mempertimbangkan konsekuensi di masa depan

Penjelasan:
Algoritma Greedy (serakah) adalah algoritma yang membuat pilihan terbaik yang tersedia pada setiap langkah dengan harapan bahwa pilihan lokal tersebut akan menghasilkan solusi global yang optimal. Namun, algoritma ini tidak selalu menjamin solusi optimal, tergantung pada masalahnya. Algoritma ini tidak mencoba semua kemungkinan dan tidak mempertimbangkan efek jangka panjang dari pilihannya.

Kalau kamu butuh contoh penerapannya, seperti dalam Greedy pada algoritma Huffman Coding atau algoritma Dijkstra (dengan syarat tertentu), tinggal bilang aja!







You said:
2. . Dalam penerapan algoritma Greedy pada game, apa yang menjadi prinsip utama dalam pengambilan keputusan?

A.

E) Menggunakan metode backtracking untuk memperbaiki kesalahan

B.

C) Memilih solusi lokal terbaik di setiap langkah dengan harapan mendapatkan solusi global terbaik

C.

B) Menggunakan rekursi untuk mencari solusi terbaik

D.

A) Mempertimbangkan semua kemungkinan solusi sebelum memilih

E.

D) Menjalankan program secara paralel untuk menemukan solusi tercepat


ChatGPT said:
Jawaban yang benar adalah:

C) Memilih solusi lokal terbaik di setiap langkah dengan harapan mendapatkan solusi global terbaik

Penjelasan:
Prinsip utama dalam algoritma Greedy, termasuk dalam penerapannya di game, adalah memilih solusi lokal terbaik (langkah terbaik saat ini) dengan harapan bahwa keputusan-keputusan tersebut akan membawa pada solusi global terbaik. Ini membuat Greedy sangat cepat dan efisien, meskipun tidak selalu menghasilkan solusi optimal dalam semua kasus.

Pilihan lainnya seperti backtracking, rekursi, dan eksplorasi paralel lebih berkaitan dengan teknik seperti brute force, divide and conquer, atau dynamic programming.







You said:
. Algoritma Greedy dapat digunakan dalam game berbasis strategi, misalnya:

A.

E) Menjalankan simulasi Monte Carlo untuk menentukan strategi terbaik

B.

C) Mengimplementasikan algoritma brute force dalam game catur

C.

A) Menentukan rute terpendek dalam game navigasi

D.

D) Menggunakan pemrograman dinamis untuk menyelesaikan teka-teki

E.

B) Menggunakan backtracking dalam puzzle Sudoku


ChatGPT said:
Jawaban yang benar adalah:

C) Menentukan rute terpendek dalam game navigasi

Penjelasan:
Dalam game berbasis strategi, algoritma Greedy sering digunakan untuk menentukan rute terpendek atau pengambilan keputusan cepat berdasarkan kondisi saat ini. Misalnya, dalam game navigasi atau permainan petualangan, karakter bisa memilih jalur yang terlihat paling menguntungkan pada setiap langkah.

Algoritma seperti Greedy Best-First Search adalah contoh penerapan dalam penentuan rute. Meskipun tidak selalu memberikan solusi optimal seperti A*, pendekatannya cepat dan efisien, cocok untuk kebutuhan real-time di banyak game.

Pilihan lain seperti brute force, backtracking, atau pemrograman dinamis bukanlah karakteristik dari pendekatan Greedy.







You said:
. Manakah dari berikut ini yang merupakan kelemahan utama dari algoritma Greedy?

A.

C) Menggunakan terlalu banyak memori

B.

E) Selalu lebih lambat daripada algoritma lain

C.

A) Selalu menghasilkan solusi optimal

D.

D) Tidak dapat digunakan dalam masalah optimasi

E.

B) Tidak selalu menghasilkan solusi optimal dalam beberapa kasus


ChatGPT said:
Jawaban yang benar adalah:

E) B) Tidak selalu menghasilkan solusi optimal dalam beberapa kasus

Penjelasan:
Kelemahan utama dari algoritma Greedy adalah bahwa ia tidak selalu menghasilkan solusi optimal, terutama jika masalah yang dihadapi tidak memiliki struktur optimal subproblem atau tidak memenuhi properti greedy-choice. Artinya, pilihan lokal terbaik di setiap langkah belum tentu mengarah ke solusi global terbaik.

Pilihan lain:

C) Menggunakan terlalu banyak memori → justru Greedy biasanya hemat memori.

E) Selalu lebih lambat → salah, Greedy biasanya lebih cepat karena tidak mengevaluasi semua kemungkinan.

A) Selalu menghasilkan solusi optimal → ini justru pernyataan yang keliru, bukan kelemahan.

D) Tidak dapat digunakan dalam masalah optimasi → salah, justru Greedy adalah salah satu pendekatan dalam masalah optimasi tertentu.

Kalau mau, aku bisa kasih contoh nyata biar lebih jelas.







You said:
5. Dalam konteks game, algoritma Greedy cocok digunakan untuk menyelesaikan masalah:

A.

D) Penyelesaian puzzle berbasis backtracking

B.

E) Pemrosesan data dalam game berbasis kecerdasan buatan

C.

C) Pemrograman dinamis dalam strategi pertempuran

D.

B) Penyelesaian game berbasis simulasi fisika

E.

A) Pencarian jalur terpendek


ChatGPT said:
Jawaban yang benar adalah:

E) A) Pencarian jalur terpendek

Penjelasan:
Dalam konteks game, algoritma Greedy sangat cocok untuk masalah pencarian jalur terpendek, terutama saat keputusan harus dibuat cepat berdasarkan informasi lokal (seperti posisi musuh, rintangan, atau tujuan).

Contoh nyata adalah:

Greedy Best-First Search dalam pencarian jalan di game strategi atau game maze.

Pemilihan power-up atau item terdekat berdasarkan nilai maksimal saat ini.

Pilihan lainnya seperti backtracking, pemrograman dinamis, atau simulasi fisika tidak sejalan dengan prinsip Greedy, karena melibatkan pendekatan yang lebih kompleks dan global, bukan hanya keputusan lokal terbaik.





## Diskusi

1. Prinsip Kerja Pemrograman Dinamik
Pemrograman dinamik (Dynamic Programming/DP) menyelesaikan masalah dengan membaginya menjadi submasalah yang lebih kecil, menyimpan hasilnya (memoisasi), dan menggunakan hasil tersebut untuk menghindari perhitungan ulang. Cocok untuk masalah yang memiliki overlapping subproblems dan optimal substructure.

2. Kompleksitas Waktu dan Ruang
Waktu: Lebih efisien daripada brute force karena submasalah dihitung satu kali. Umumnya O(n) atau O(n²) tergantung masalah.

Ruang: Bergantung pada penyimpanan hasil submasalah, biasanya O(n). Namun bisa dioptimalkan jadi O(1) dengan teknik tabulasi dan space optimization.

3. Contoh Penerapan
Fibonacci (menghindari perhitungan berulang)

Knapsack Problem (maksimalkan nilai dalam kapasitas tertentu)

Edit Distance (mengukur kemiripan dua string)

Longest Common Subsequence (LCS)


## Posttest

Mengapa algoritma Greedy tidak selalu memberikan solusi optimal dalam semua masalah?

A.

Karena hanya berfokus pada solusi terbaik saat ini tanpa mempertimbangkan konsekuensi jangka panjang

B.

Karena membutuhkan komputasi yang sangat kompleks

C.

Karena selalu mempertimbangkan seluruh kemungkinan solusi

D.

Karena bergantung pada struktur data yang digunakan

E.

Karena hanya digunakan dalam masalah matematika


ChatGPT said:
Jawaban yang benar adalah:

A. Karena hanya berfokus pada solusi terbaik saat ini tanpa mempertimbangkan konsekuensi jangka panjang

Penjelasan:
Algoritma Greedy memilih langkah yang tampak terbaik pada saat itu (lokal optimal), tanpa memikirkan apakah keputusan tersebut akan membawa pada solusi global yang optimal. Ini bisa menyebabkan hasil akhir yang suboptimal, terutama jika masalah tersebut tidak memenuhi greedy-choice property atau optimal substructure.

Pilihan lain tidak tepat karena:

B → Greedy justru dikenal sederhana dan cepat.

C → Itu ciri brute force, bukan Greedy.

D → Greedy tidak tergantung penuh pada struktur data tertentu.

E → Greedy digunakan luas, bukan hanya dalam matematika.


Dalam permainan berbasis strategi, algoritma Greedy sering digunakan untuk:

A.

Mengimplementasikan kecerdasan buatan berbasis pembelajaran mesin

B.

Memastikan game berjalan tanpa bug

C.

Menggunakan pemrograman dinamis untuk mencari solusi terbaik

D.

Memprediksi pergerakan lawan dalam permainan catur

E.

Menentukan langkah optimal di setiap giliran permainan


ChatGPT said:
Jawaban yang benar adalah:

E. Menentukan langkah optimal di setiap giliran permainan

Penjelasan:
Dalam game strategi, algoritma Greedy sering digunakan untuk memilih langkah terbaik yang tersedia pada saat itu, tanpa memperhitungkan dampaknya di masa depan. Ini membuat Greedy cocok untuk pengambilan keputusan cepat dalam setiap giliran, seperti menyerang musuh terlemah atau mengambil item terdekat.

Pilihan lain:

A → Itu lebih ke ranah machine learning, bukan Greedy.

B → Terkait pengujian/debugging, bukan algoritma.

C → Pemrograman dinamis berbeda prinsip dengan Greedy.

D → Prediksi pergerakan biasanya melibatkan tree search atau minimax, bukan Greedy.


Algoritma Dijkstra adalah salah satu contoh algoritma Greedy yang digunakan untuk:

A.

Menentukan urutan eksekusi tugas dalam sistem operasi

B.

Mencari jalur terpendek dalam sebuah graf

C.

Menggunakan pemrograman dinamis dalam optimasi inventaris

D.

Menganalisis kemungkinan langkah dalam permainan kartu

E.

Menyelesaikan teka-teki Sudoku


ChatGPT said:
Jawaban yang benar adalah:

B. Mencari jalur terpendek dalam sebuah graf

Penjelasan:
Algoritma Dijkstra adalah contoh algoritma Greedy yang digunakan untuk mencari jalur terpendek dari satu simpul ke simpul lainnya dalam sebuah graf berbobot non-negatif. Pada setiap langkah, algoritma ini memilih simpul dengan jarak terpendek yang belum dikunjungi — keputusan lokal terbaik yang mendekati solusi global.

Pilihan lain tidak tepat karena:

A → Penjadwalan tugas biasanya menggunakan algoritma lain seperti round-robin atau priority scheduling.

C → Itu lebih cocok untuk pemrograman dinamis.

D dan E → Lebih ke backtracking atau pencarian ruang status, bukan Greedy.

Mau aku tunjukin ilustrasi cara kerja Dijkstra juga?

Manakah dari berikut ini yang merupakan contoh implementasi algoritma Greedy dalam game?

A.

Menggunakan simulasi Monte Carlo dalam strategi permainan

B.

Menggunakan pemrograman dinamis untuk perhitungan skor optimal

C.

Menyelesaikan game catur dengan backtracking

D.

Menganalisis pola permainan menggunakan pembelajaran mesin

E.

Pemilihan jalur tercepat dalam game pacuan mobil


Jawaban yang benar adalah:

**E. Pemilihan jalur tercepat dalam game pacuan mobil**

### Penjelasan:
**Algoritma Greedy** dalam game sering digunakan untuk memilih **jalur tercepat atau terbaik** secara lokal, seperti dalam **game pacuan mobil**, di mana kendaraan memilih jalur yang terlihat paling menguntungkan saat itu. Ini adalah contoh nyata penerapan prinsip Greedy: **keputusan cepat dan efisien berbasis kondisi saat ini**.

Pilihan lain:
- **A** → Monte Carlo lebih ke simulasi dan statistik.
- **B** → Pemrograman dinamis, bukan Greedy.
- **C** → Backtracking, bukan pendekatan Greedy.
- **D** → Pembelajaran mesin (machine learning), beda ranah.

Mau daftar lebih banyak contoh game yang pakai Greedy?

Algoritma Greedy lebih cocok digunakan untuk menyelesaikan masalah yang memiliki:

A.

Kompleksitas tinggi yang memerlukan eksplorasi seluruh solusi

B.

Struktur keputusan berbasis rekursi

C.

Kebutuhan untuk mencari solusi terbaik dengan pendekatan backtracking

D.

Sifat optimalitas lokal yang menghasilkan solusi global optimal

E.

Struktur data berbasis graf yang memerlukan pencarian menyeluruh


Jawaban yang benar adalah:

**D. Sifat optimalitas lokal yang menghasilkan solusi global optimal**

### Penjelasan:
**Algoritma Greedy** lebih cocok digunakan untuk masalah yang memiliki **sifat optimalitas lokal**, yaitu masalah di mana pilihan terbaik pada setiap langkah lokal (pilihan terbaik saat ini) akan menghasilkan solusi yang optimal secara global. Greedy memanfaatkan prinsip ini untuk menemukan solusi secara cepat tanpa mengevaluasi semua kemungkinan.

Pilihan lain:
- **A** → Kompleksitas tinggi biasanya membutuhkan algoritma lain seperti brute force atau pemrograman dinamis.
- **B** → Greedy tidak selalu berbasis rekursi.
- **C** → Backtracking adalah teknik yang berbeda dari Greedy.
- **E** → Untuk masalah graf yang memerlukan pencarian menyeluruh, lebih sering digunakan algoritma seperti DFS atau BFS, bukan Greedy.

Kalau ada contoh lainnya yang perlu dibahas, tinggal bilang ya!
