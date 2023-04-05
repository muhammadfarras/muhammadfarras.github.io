---
hide:
  - footer
---
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

**Keuntungan menggunakan recursion**

1.  Penggunaan recursive function membuat kode terlihat lebih keren dan elegan
2.  Tugas kompleks dapat dipecah menjadi masalah kecil menggunakan recursive function
3.  Squance generation lebih mudah dilakukan dari pada menggunakna iteration (perulangan).

**Keburukan dari recursion**

1.  Seringkali logika dibalik recursive sangat sulit untuk dipahami
2.  Pemanggilan recursive memakan waktu dan tempat penyimpanan yang lebih banyak
3.  Recursive function sangat sulit untuk didebug jika terjadi masalah.


## Implementasi nyata fungsi `#!python generator.throw()`
Source : [Stack Overflow](https://stackoverflow.com/a/11487070/11021522)

Let's say I use a generator to handle adding information to a database; I use this to store network-received information, and by using a generator I can do this efficiently whenever I actually receive data, and do other things otherwise.

So, my generator first opens a database connection, and every time you send it something, it'll add a row:

```python
def add_to_database(connection_string):
    db = mydatabaselibrary.connect(connection_string)
    cursor = db.cursor()
    while True:
        row = yield
        cursor.execute('INSERT INTO mytable VALUES(?, ?, ?)', row)
```

That is all fine and well; every time I `#!python .send()` my data it'll insert a row.

But what if my database is [transactional](../../DBMS/Catatan%20MySql/07.%20Modifiying%20data%20and%20Tabel%20Structure.md#using-transactions-to-save-or-revert-changes)? How do I signal this generator when to commit the data to the database? And when to abort the transaction? Moreover, it is holding an open connection to the database, maybe I sometimes want it to close that connection to reclaim resources.

This is where the `#!python .throw()` method comes in; with `#!python .throw()` I can raise exceptions in that method to signal certain circumstances:

```python
def add_to_database(connection_string):
    db = mydatabaselibrary.connect(connection_string)
    cursor = db.cursor()
    try:
        while True:
            try:
                row = yield
                cursor.execute('INSERT INTO mytable VALUES(?, ?, ?)', row)
            except CommitException:
                cursor.execute('COMMIT')
            except AbortException:
                cursor.execute('ABORT')
    finally:
        cursor.execute('ABORT')
        db.close()
```

The `#!python .close()` method on a generator does essentially the same thing; it uses the GeneratorExit exception combined with `#!python .throw()` to close a running generator.

All this is an important underpinning of how coroutines work; coroutines are essentially generators, together with some additional syntax to make writing a coroutine easier and clearer. But under the hood they are still built on the same yielding, and sending. And when you are running multiple coroutines in parallel, you need a way to cleanly exit those coroutines if one of them has failed, just to name an example.
