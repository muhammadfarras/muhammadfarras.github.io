# Control Processing Unit dan Graphical Processing Unit

## Persamaan CPU dan GPU

:   `Unit Pemprosesan (_Porcessor_)`

* Baik CPU (_Central Processing Unit_) dan GPU (_Graphical Processing Unit_) adalah unit pemprosesan yang dirancang untuk {==melakukan kalkulasi==} dan {==mengeksekusi instruksi==}.

:   `Memiliki Core Inti`

* Keduanya memiliki jumlah core, walaupun jumlah core dari keduanya berbeda-beda.

:   `Berfungsi untuk komputasi`

* Keduanya digunakan untuk menjalankan komputasi, baik itu _general purpose_ (CPU) dan _pararel processing_ (GPU).

:   `Memiliki Memory Controller`

* CPU dan GPU, keduanya mengelola memori untuk menyimpan dan memproses data.

### Perbedaan CPU dan GPU

| Aspek | CPU | GPU |
| :---- | :---- | :---- |
| **Fungsi Utama** | Mengelola dan mengeksekusi instruksi umum (_general-purpose processing_) | Mengelola komputasi `pararel` (Grafis, video, AI, Scientific Computing)|
| **Jumlah Core** | Lebih sedikit, biasanya antara 4 core - 16 Core | Memiliki banyak core, hingga ribuan core|
| **Arsitektur Core** | Kompleks, mampu menangani bergai instruksi | Sederhana, dimaksimalkan untuk kalkulasi pararel |
| **Kecepatan Clock** | Tingg (2 ~ 4 GHZ) | Lebih rendah dibandingkan dengan CPU (1 ~ 2 GHZ) |
| **Komputasi Pararel** | Terbatas pada multithreading | Sangat kuat untuk komputasi pararel (_multi threading_). `SIMD`, _Single Instruction Multiple Data_|
| **Tugas Utama** | Menjalankan Operating System, aplikasi umum, kontrol Input/Output | Rendering Grafis, Machine Learning, Kriptogradi, dan simulasi |
| **Latency dan Respons** | Rendah (Respone cepat untuk tugas single thread) | Tinggi (Respone cepat untuk tugas multi thread) |

## Cara Kerja CPU

1. `Fetch` - Mengambil instruksi dari memori (RAM).
2. `Decode` - mengubah instruksi menjadi sinyak yang bisa dipahami oleh `unit controll CPU`.
3. `Execute` - Melakukan perhitungan atau instruksi di **ALU** (_Arithmetic Logic Unit_).
4. `Writeback` - Menyimpan hasil eksekusi ke memori atau register.
5. `Control & Scheduling` - CPU memiliki control unit yg bertugas untuk ;
    a. Mengatur jalannya proses
    b. Mengatur _interrupt_
    c. _Multitasking_ dengan sistem operasi

### Kelebihan CPU

* Fleksibel, dapat menjalankan berbagai jenis perintah.
* Cocok untuk task yang membutuhkan instruksi berurutan.
* Cepat dalam mengakses memori utama.

## Cara Kerja GPU

1. `Masive Parallelism` - GPU memliki ratusan hingga ribuan core yang bekerja secara pararel.
2. `Single Instruction Multiple Data (SIMD) Model` - Menjalankan instruksi yang sama secara bersamaan pada banyak data (Rendering, Grafis).
3. `Pipelining & Batch Processing` - memproses data dalam batch besar dengan pipeline yang dioptimalkan.
4. `Specialized Memory Access` - GPU memiliki memori sendiri, yaitu VRAM, yang dapat diakses lebih cepat oleh core-core-nya.

### Kelebihan GPU

* Sangat efesien untuk komputasi data besar secara pararel (Data Training, Deep Learning)
* Lebih tinggi througout dari pada CPU untuk tugas-tugas yang dilakukan pararel.
