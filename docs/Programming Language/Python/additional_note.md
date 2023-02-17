## Recursion
Source : [https://www.programiz.com/python-programming/recursion](https://www.programiz.com/python-programming/recursion)

Di python, sebuah fungsi dapat memanggil fungsi lainnya. Fungsi tersebut juga dapat memanggil dirinya sendiri. Gambar dibawah ini menjelaskan bagaimana recursive function bekerja.

![konsep recursive function](aset/an.%20konsep%20recursive.png)

Dibawah ini adalah contoh penggunaan recursive function untuk menemukan fakotrial dari sebuah angka. Misalkan faktorial dari 6 (ditandai dengan $6!$ ) `1 x 2 x 3 x 4 x 5 x 6 = 720`

!!! code
    ```python
    def factorial(x):
        """This is a recursive function
        to find the factorial of an integer"""

        if x == 1:
            return 1
        else:
            return (x * factorial(x-1))


    num = 3
    print("The factorial of", num, "is", factorial(num))
        ```

    ```{.pyton .no-copy title="Print Output"}
    The factorial of 3 is 6
    ```

Penjelasan langkah-langkah fungsi `factorial()` diatas:

![Step by Step recursive](aset/an.%20python-factorial-function.png)

### Keuntungan menggunakan recursion

1.  Penggunaan recursive function membuat kode terlihat lebih keren dan elegan
2.  Tugas kompleks dapat dipecah menjadi masalah kecil menggunakan recursive function
3.  Squance generation lebih mudah dilakukan dari pada menggunakna iteration (perulangan).

### Keburukan dari recursion

1.  Seringkali logika dibalik recursive sangat sulit untuk dipahami
2.  Pemanggilan recursive memakan waktu dan tempat penyimpanan yang lebih banyak
3.  Recursive function sangat sulit untuk didebug jika terjadi masalah.