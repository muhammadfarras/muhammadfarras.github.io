# Brute Force Algorithm dan Exhaustive Search

## Time Complexity

Record the start time and record the end time and get the running time. Tidak cara baik untuk mengitung, karena hardware yang berbeda-beda ketika mengimplementasi algoritma tersebut, sehingga bukan cara yg tepat untuk mengukur kemampuan algoritma.Maka kita membutuhkan cara yang lebih objektif, yaitu dengan, melihaat banyak langkah yang dilakukan oleh sebuah algoritma dalam menyelesaikan operasinya, inilah yang disebut dengan Time Complexity

Akan sangat berguna bagi kita jika dapat membandingkan antara performa dari beberapa algoritma untuk mengetahui algoritma mana yang lebih baik. Salah satu cara yang terlintas pertama kali bagi kebanyakan orang adalah dengan cara mencatatan waktu awal proses ketika algoritma berjalan dan waktu ketika proses tersebut berakhir, lalu kita menghitung selisih antara waktu tersebut sehingga menghasilkan waktu yang dipakai oleh algoritma untuk menyelesaikan operasinya. Namun, hal tersebut kurang tepat, karena terpengaruhi oleh variabel lain, yaitu hardware yang digunakan. Bisa jadi algoritma yang paling tidak efesien yang dijalankan pada kompter dengan ram tinggi dan CPU terbaik akan menghasilkan waktu singkat. Maka dari itu kita membutuhkan cara lain yang lebih objektif untuk mengukur performa algoritma. Yaitu dengan cara melihat sebarapa banyak langka yang dilakukan oleh sebuah algoritma dalam menyelesaikan operasinya. Inilah yang disebut dengan Time Complexity.

Lalu menyangkut dengan pentingnya, Time Complexity menjadi patokan yang tidak kalah penting dengan hasil keluaran dari sebuah algoritma, didukung diera big data, pengolahan data pada sebuah proses memnjadi hal yang tidak disepelekan. Maka dari itu menghitung komplesitas waktu sebuah algoritma dalam pengembangan sebuah program menjadi hal yang tidak boleh dikesampingkan.

[https://www.udemy.com/course/data-structures-and-algorithms-deep-dive-using-java/learn/lecture/8435752#notes](https://www.udemy.com/course/data-structures-and-algorithms-deep-dive-using-java/learn/lecture/8435752#notes)

## Big On Notation

| Big-O | Desc of time |
| :---- | :----- |
| $O(1)$ | Constant |
| $O(Log n)$ | log n |
| $O(n)$ | Linear |
| $O(n log n)$ |n log-star n|
| $O(n^2)$ | Quandratic|

## Big-O, Big-Tetha, Big-Mega

Big-O Notation : Merepresentasikan batas atas dari waktu yang dihabiskan oleh sebuah algoritma dalam menjalankan operasinya. Maka dari itu notasi ini menggambarkan kompleksitas kemungkinan terburuk dari sebuah algoritma

Omega Notation : Merepresentasikan batas bawah dari waktu yang dihabiskan oleh sebuah algoritma dalam menjalankan operasinya. Maka dari itu notasi ini menggambarkan kompleksitas kemungkinan terbaik dari sebuah algoritma

Theta Notation : Merepresentasikan batas atas dan bawah dari waktu yang dihabiskan oleh sebuah algoritma dalam menjalankan operasinya. Maka dari itu notasi ini menggambarkan kompleksitas rata-rata dari sebuah algoritma

Dari 3 notasi diatas dalam menghitung secara objektif waktu yg ditempuh sebuah algoritma, maka Big-O adalah yang paling banyak digunakan untuk menganlisa sebuah algoritma karena menghitung kemungkinan terburuk lebih menjamin dibandingkan dengan the best atau average skenarion.

[https://www.programiz.com/dsa/asymptotic-notations](https://www.programiz.com/dsa/asymptotic-notations)

## Space Complexity

Kompleksitas ruang sebuaha algortima adalah jumlah ruang yang dibutuhkan sebuah algoritma berdsarakan besaran nilai masukan. Kompleksitas ruang ini termasuk didalamnya adalah _Auxiliary space_ dan ruang yang digunakan oleh nilai inputan.

Komplesitas ruang konsep yang berjalan bersamaan dengan komplesitas waktu, jika kita membuat sebuah array dengan ukuran _n_, maka ruang yang dibutuhkan adalah O(n), lalu jika nested array atau dua dimensi array maka membutuhkan O(n^2).

Saya menyingung _Auxiliary space_, berbeda pada setiap bahasa pemprograman dalam ruang digunakan, namun secara umumr adalah ekstra space, tempat penyimpanan sementara yang digunakan oleh sebuah algoritma. Jika di java ada istilah heap dst.

[https://www.geeksforgeeks.org/g-fact-86/](https://www.geeksforgeeks.org/g-fact-86/)
[https://stackoverflow.com/a/22234095/11021522](https://stackoverflow.com/a/22234095/11021522)

## Brute Force

Adalah salah algoritma paling sederhana dalam sebuah pemecahan masalah. Sebagaimana artinya, metode ini adalah cara yang kasar dan memaksa, dimana bisa kita katakan dengan istiliah algoritma _Just Do It_. Seperti sebuah angka dalam sebuah kumpulan data, maka metode ini akan melihat kesemua data dan mengebalikan hasilnya jika match. Namun dibalik itu semua, metode ini sangat jelas, mudah dimengerti dan sangat sederhana. Biasanya metode _Brute Force_ membutuhkan langkah $O(n)$, atau langkahnya sebanyak dengan jumlah data.

### kekuatan

1. _wide capability_, Metode _Brute Force_ dapat digunakan hampir disemua masalah.
2. Sederhana dan mudah dimengerti.

### Kelemahan

1. Memerlukan waktu dan ruang yang lebih besar dibandingkan algoritma yang lebih cerdas.

### Contoh

!!! notes "Mencari Elemen Terbesar"

    ```python
    langkah = 0
    def elemenTerbesar(list = [] ):

        global langkah

        nilai_terbesar = 0
        for a in list:
            # Get number of steps
            langkah+=1

            if a > nilai_terbesar:
                nilai_terbesar = a
            
        return nilai_terbesar

    print(f'Nilai terbesar {elemenTerbesar(range(0,50,3))}')
    print(f'Number of step {langkah}')
    ```

!!! notes "Faktorial"

    ```python
    langkah = 1
    def faktorial(number=1):
        global langkah
        result  = number
        for a in range(1, number):
            langkah+=1
            result = result * a

        return result


    n = 4
    print(f'Faktorial {n} adalah {faktorial(n)}') # 24
    print(f'Number of step {langkah}') # 4
    ```

    Atau kita bisa menggunakan recursive function, more detail lihat [disini](/docs/Programming%20Language/Python/additional_note.md#Recursion)

    ```python
    def recursive(x):
        if x in range (0,1):
            return 1
        
        return recursive(x-1) * x

    print(recursive(3))
    ```
